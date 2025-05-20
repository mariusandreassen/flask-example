# ─── STAGE 1: Build your Next.js frontend ─────────────────────────────────────
FROM node:18-alpine AS frontend-builder
WORKDIR /app/frontend

# 1. install deps & build
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm ci
COPY frontend/ ./
RUN npm run build \
    && npm run export            

# ─── STAGE 2: Build & test your Flask backend ─────────────────────────────────
FROM python:3.10-slim AS backend-builder
WORKDIR /app

# 1. install both runtime + dev deps
COPY backend/requirements.txt backend/requirements-dev.txt ./
RUN pip install --user -r requirements.txt -r requirements-dev.txt

# 2. copy your Flask app & tests
COPY backend/app/ ./app
COPY backend/tests/ ./tests

# 3. run pytest, fail if coverage <100%
RUN pytest --maxfail=1 --disable-warnings --exitfirst \
    --cov=app --cov-fail-under=100

# ─── STAGE 3: Build your final runtime image ──────────────────────────────────
FROM python:3.10-slim
WORKDIR /app
ENV PATH=/root/.local/bin:$PATH

# 1. pull in only the installed Python packages
COPY --from=backend-builder /root/.local /root/.local

# 2. copy Flask code
COPY backend/app/ ./app
# if you need Firebase Admin:
COPY backend/serviceAccountKey.json ./

# 3. copy Next.js static build into Flask’s static folder
COPY --from=frontend-builder /app/frontend/out ./app/static

EXPOSE 8000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
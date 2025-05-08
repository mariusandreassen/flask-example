# Use official Python base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first to cache dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "run.py"]
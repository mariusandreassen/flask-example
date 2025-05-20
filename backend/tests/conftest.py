import sys, os

root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
)
if root not in sys.path:
    sys.path.insert(0, root)
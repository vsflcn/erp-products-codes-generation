# Use the Python base image
FROM python:3.9-slim

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code
COPY . .

# Run the application
CMD ["python", "app.py"]

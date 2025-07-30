# Use official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src

# Set environment variable for project root
ENV PROJECT_ROOT=/app

# Run extraction when container is executed
CMD ["python", "-m", "src.run_pipeline"]
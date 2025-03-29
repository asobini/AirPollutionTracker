FROM python:3.10-slim

WORKDIR /app

# Install dependencies as root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user and set permissions
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Copy application code as non-root user
COPY . .
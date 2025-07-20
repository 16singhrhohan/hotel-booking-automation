# Use official Python base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy project files into container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Command to run tests when container starts
CMD ["pytest", "--maxfail=1", "--disable-warnings"]

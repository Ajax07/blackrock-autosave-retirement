# docker build -t blk-hacking-ind-ajay .
# Using python:3.11-slim (lightweight Linux base image for performance and security)

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Required port from challenge
EXPOSE 5477

# Start FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5477"]

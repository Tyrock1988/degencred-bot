FROM python:3.11-slim

# Install system packages needed for Pillow
RUN apt-get update && apt-get install -y libjpeg-dev zlib1g-dev

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files into the container
COPY . .

# Expose the port your app runs on
EXPOSE 8080

# Use Uvicorn to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

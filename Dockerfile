# Use Python base image
FROM python:3.9

# Set an environment variable for detecting Docker
ENV DOCKER_ENV=1

# Set the working directory inside the container
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 4000

# Run the application
CMD ["python", "app.py"]

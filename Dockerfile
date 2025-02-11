# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 1000

# Run Flask app
CMD ["python", "app.py"]

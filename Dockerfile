# Use the official Python image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your code and the requirements.txt file to the container
COPY . /app/

# Install the necessary dependencies  
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run your Flask application
CMD ["python", "app.py"]

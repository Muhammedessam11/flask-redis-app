# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Flask app's port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]


FROM python:3.12-slim

WORKDIR /app

# Copy your Python requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code to the container
COPY . .

# Set the FLASK_APP environment variable
ENV FLASK_APP=telegram_sender.py

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

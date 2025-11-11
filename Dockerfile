# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Remove selenium and related packages from requirements.txt for Docker build
RUN sed -i '/selenium/d; /undetected-chromedriver/d; /trio-websocket/d; /websocket-client/d; /websockets/d' requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY . .

# Define the command to run your application
CMD ["python", "main.py"]

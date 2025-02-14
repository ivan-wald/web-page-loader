# Use the official Python image from the Docker Hub.
FROM python:3.12-slim

# Set the working directory.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY ./app /app
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches.
CMD ["python", "app.py"]
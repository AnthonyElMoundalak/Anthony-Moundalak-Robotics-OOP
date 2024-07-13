# Use the official Python image from the Docker Hub as the base image
#
FROM python:3.9-slim 

# Set the working directory in the container to /src
#
WORKDIR /src

# Copy the current directory contents into the container at /src
#
COPY ./src .

# COPY ./test ../test

# Install any needed packages specified in requirements.txt
#
# RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
#
EXPOSE 5000

# Define environment variable
#

# Run app.py when the container launches
#
CMD ["python", "main.py"]

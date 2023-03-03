# Use an official Python runtime as a parent image
FROM arm32v7/python:2.7.13-jessie

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt

COPY requirements.txt /
RUN pip install -r /requirements.txt
#RUN pip install --no-cache-dir rpi.gpio 


# Run app.py when the container launches
CMD ["python", "./app.py"]

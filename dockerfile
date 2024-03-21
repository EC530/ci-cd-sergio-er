# Start by pulling the base image
FROM python:3.11-slim

# Set the working directory to /app in the container
WORKDIR /.

# Copy the current directory into the /app container directory
COPY . /.

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Run pytest to execute tests
#RUN pytest

# The command to run the application when the container starts
CMD ["python", "./MatrixMult.py"]

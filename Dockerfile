# Use the official Python base image
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and requirements.txt into the container
COPY todo_list.py requirements.txt /app/

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point for the container to run your Python script
CMD ["python", "todo_list.py"]

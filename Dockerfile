# Use the official Python image from the Docker Hub
FROM python:3.12.1

# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port your app runs on (default for Django)
EXPOSE 8000

# Command to run your application using Django's built-in server (for development)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Project.wsgi:application"]
# CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "Project.wsgi:application"]
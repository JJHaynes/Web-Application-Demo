# Use an official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY .. /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

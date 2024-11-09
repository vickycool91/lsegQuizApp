# Use Python slim image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy files
COPY . /app

# Copy the questions.json file into the working directory inside the container
COPY app/questions.json /app/

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 8082

# Run the application
CMD ["python", "app/main.py"]

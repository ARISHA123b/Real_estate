# Base image with Python (change version if needed)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your project files into the container
COPY . .

# Install dependencies
COPY requirement.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port if your app runs on one (e.g., Gradio or Flask)
EXPOSE 7860

# Command to run your application (replace as needed)
CMD ["python", "tasks.py"]

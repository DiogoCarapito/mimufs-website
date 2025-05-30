# Use an official Python runtime as a parent image
FROM python:3.12.5-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Streamlit will run on (default is 8501)
EXPOSE 8501

# Run your Streamlit app when the container is started
ENTRYPOINT ["streamlit", "run", "mimufs.py", "--server.port=8501", "--server.address=0.0.0.0"]

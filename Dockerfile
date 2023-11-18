# Set arguments
ARG BASE_CONTAINER=python:3.12-alpine

# Set the base image.
FROM --platform=linux/amd64 $BASE_CONTAINER

# Sets the user name to use when running the image.
USER root

# Make a directory for our app
WORKDIR /consumer

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy our source code
COPY /src ./consumer
COPY /configs ./configs

# Run the application
CMD ["python", "-m", "consumer"]

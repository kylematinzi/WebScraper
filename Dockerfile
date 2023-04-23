# Dockerfile, Image, Container
# Dockerfile - a bluprint for building images.
# Image - template for running containers.
# Container - packaged project. The thing thats actually running.

# Have to define the docker file.
# Specify a base image. This adds python to the container.
FROM python:3.10

# Add the program to the container
ADD main.py .

# Install the programs dependencies
RUN pip install requests beautifulsoup4

# Specify entry command
# This will run python and then the main.py class
CMD ["python", "./main.py"]
# Pull Base Image
FROM python:3.10.4-slim-bullseye

# Set enviroment variables 
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create a root directory for our project in container
RUN mkdir /techwondoetask
# Set working directory
WORKDIR /techwondoetask

# Install depenedencies
COPY ./requirements.txt /techwondoetask/
RUN pip install -r requirements.txt

# Copy project
COPY . /techwondoetask/
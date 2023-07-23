FROM python:3.11

ENV LANG=C.UTF-8

# Copy files
RUN mkdir -p /opt/app/
COPY requirements.txt /opt/app/
COPY install_dependencies.sh /opt/app/

# Install dependencies
RUN cd /opt/app/ && \
    bash ./install_dependencies.sh ./requirements.txt

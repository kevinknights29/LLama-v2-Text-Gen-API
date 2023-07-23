FROM python:3.11

ENV LANG=C.UTF-8

# Copy files
RUN mkdir -p /opt/app/
COPY requirements.txt /opt/app/
COPY install_dependencies.sh /opt/app/

# Download models
RUN mkdir -p /opt/app/models/ && \
    cd /opt/app/models/ && \
    wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_0.bin

# Install dependencies
RUN cd /opt/app/ && \
    bash ./install_dependencies.sh ./requirements.txt

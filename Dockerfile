FROM python:3.11.4-slim-bullseye

ENV LANG=C.UTF-8 \
    PYTHONPATH=${PYTHONPATH}:/opt/app.

# Set working directory
WORKDIR /opt/app

# Install packages
RUN apt update && \
    apt install -y --no-install-recommends \
    wget \
    git \
    build-essential \
    python3-launchpadlib

# Download models
RUN mkdir -p models && \
    cd models && \
    wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_0.bin

# Copy files
COPY requirements.txt \
    main.py \
    ./
COPY src src/

# Install dependencies
RUN python -m pip install --upgrade pip && \
    python -m pip install -r ./requirements.txt

# Run Flask App
EXPOSE 7860
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=7860"]

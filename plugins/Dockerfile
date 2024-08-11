FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libgthread-2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app


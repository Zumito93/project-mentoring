FROM ubuntu:22.04

# Python
RUN apt update \
    && apt install -y --no-install-recommends python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Project user
RUN useradd -U santiago

# Project directory
WORKDIR /project-mentoring

# Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Switch user
USER santiago:santiago

# Copy code
COPY --chown=santiago:santiago . .

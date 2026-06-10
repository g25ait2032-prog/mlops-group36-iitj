# -----------------------------------------------------------------------
# Task 6: Dockerfile — slim inference image
# -----------------------------------------------------------------------
# 1. Start with the base image (This MUST be first!)
FROM python:3.10-slim

# 2. Define Build Arguments
ARG HF_TOKEN
ARG HF_MODEL_NAME=nagaananth/MLOPS_group-v2

# 3. Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HF_MODEL=${HF_MODEL_NAME}
ENV HF_TOKEN=${HF_TOKEN}
WORKDIR /app

# Install only inference dependencies (no training libs)
COPY requirements.txt .
RUN pip install --no-cache-dir \
        transformers==4.41.2 \
        torch==2.3.0 \
        huggingface-hub==0.23.2 \
        accelerate==0.30.0

# Copy inference script
COPY src/inference.py /app/inference.py

# Pre-download model weights at build time (optional — makes runtime faster)
# Remove this RUN block if image size is a concern
RUN python -c "from transformers import pipeline; pipeline('text-classification', model='${HF_MODEL_NAME}', device=-1)"

CMD ["python", "inference.py"]

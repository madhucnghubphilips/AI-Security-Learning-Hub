FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /workspace/Lab

COPY Lab/app/requirements.txt /tmp/chatbot-requirements.txt
RUN python -m pip install --upgrade pip \
    && python -m pip install -r /tmp/chatbot-requirements.txt

COPY Lab/app ./app

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.rag_server:app", "--host", "0.0.0.0", "--port", "8000"]

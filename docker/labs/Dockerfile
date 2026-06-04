FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

WORKDIR /workspace

COPY docker/labs/requirements.txt /tmp/labs-requirements.txt
RUN python -m pip install --upgrade pip \
    && python -m pip install -r /tmp/labs-requirements.txt

COPY LLM01 ./LLM01
COPY LLM02 ./LLM02
COPY LLM03 ./LLM03
COPY LLM04 ./LLM04
COPY LLM05 ./LLM05
COPY LLM06 ./LLM06
COPY LLM07 ./LLM07
COPY LLM08 ./LLM08
COPY LLM09 ./LLM09
COPY LLM10 ./LLM10
COPY docker/labs/start-labs.sh /usr/local/bin/start-labs.sh

EXPOSE 8501 8502 8503 8504 8505 8506 8507 8508 8509 8510

CMD ["/bin/sh", "/usr/local/bin/start-labs.sh"]

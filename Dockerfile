
FROM python:3.7-slim

WORKDIR /app

COPY ./Pipfile* ./

RUN pip install pipenv && \
    apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
    pipenv install --deploy --system && \
    apt-get remove -y gcc python3-dev libssl-dev && \
    apt-get autoremove -y && \
    pip uninstall pipenv -y \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8501

COPY ./.streamlit ./.streamlit
COPY ./src ./src
COPY ./startapp.sh ./startapp.sh
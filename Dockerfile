FROM python:3.11-slim

WORKDIR /app

# Instalar dependências para cx_Oracle
RUN apt-get update && apt-get install -y \
    libaio1 \
    gcc \
    unzip \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# ⬇️ Usar instantclient.zip local (coloque na raiz do projeto)
COPY instantclient.zip .

RUN mkdir -p /opt/oracle && \
    unzip instantclient.zip -d /opt/oracle && \
    rm instantclient.zip && \
    echo "/opt/oracle/instantclient_23_8" > /etc/ld.so.conf.d/oracle-instantclient.conf && \
    ldconfig

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_23_8
ENV PATH=$PATH:/opt/oracle/instantclient_23_8

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app/src

ENTRYPOINT ["python", "src/entrypoint.py"]
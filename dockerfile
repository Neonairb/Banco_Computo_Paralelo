FROM python:3.9

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Instalar requisitos previos de Oracle
RUN apt-get update && apt-get install -y gcc && apt-get install -y libaio1 wget unzip && \
    mkdir /opt/oracle

# Descargar el archivo ZIP de Oracle Instant Client
RUN wget https://download.oracle.com/otn_software/linux/instantclient/199000/instantclient-basic-linux.x64-19.9.0.0.0dbru.zip \
    -O /opt/oracle/instantclient-basic-linux.x64-19.9.0.0.0dbru.zip

# Descomprimir el archivo ZIP de Oracle Instant Client
RUN cd /opt/oracle && \
    unzip instantclient-basic-linux.x64-19.9.0.0.0dbru.zip && \
    rm instantclient-basic-linux.x64-19.9.0.0.0dbru.zip && \
    echo /opt/oracle/instantclient_19_9 > /etc/ld.so.conf.d/oracle-instantclient.conf && \
    ldconfig
    
COPY requirements.txt /app
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code into container
COPY . /app

# Expose application port
EXPOSE 8501

# Set application entry point
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

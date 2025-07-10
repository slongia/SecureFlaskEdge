FROM python:3.10-slim-bullseye
WORKDIR /app
COPY . .
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y redis-server && \ 
    apt-get clean && \     
    rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["gunicorn", "app:app", "--config", "gunicorn_config.py"]
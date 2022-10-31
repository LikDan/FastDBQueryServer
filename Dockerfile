FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app

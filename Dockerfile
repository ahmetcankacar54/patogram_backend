FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
ENV   PYTHONUNBUFFERED 1
COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]

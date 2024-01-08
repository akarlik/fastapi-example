FROM python:3.11-alpine

ADD . /app
ADD requirements.txt /app/reqs.txt

RUN pip install --no-cache-dir --upgrade -r /app/reqs.txt

WORKDIR /app

CMD ["python", "app.py"]
EXPOSE 3000
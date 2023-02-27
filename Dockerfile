FROM python:slim-buster

WORKDIR /app

COPY . .

RUN mkdir /var/log/gunicorn

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "config/gunicorn.py"]
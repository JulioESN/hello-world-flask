
FROM python:3.9.20-alpine3.19

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD [ "python3", "app.py" ]
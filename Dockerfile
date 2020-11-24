FROM python:3.9

WORKDIR /sample

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python", "./server.py" ]

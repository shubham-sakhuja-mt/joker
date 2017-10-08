FROM python:2.7.10

RUN pip install web.py

COPY ./ /app/
WORKDIR /app

CMD python -u /app/serve.py

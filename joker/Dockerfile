FROM python:2.7.18

RUN pip install web.py==0.51 requests

COPY serve.py ./

CMD exec python -u serve.py

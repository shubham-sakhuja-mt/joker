FROM python

RUN pip3 install web.py==0.61 requests

COPY jokes.json serve.py ./

CMD exec python -u serve.py

FROM python

RUN pip3 install web.py==0.61 requests

COPY serve.py ./

CMD exec python -u serve.py

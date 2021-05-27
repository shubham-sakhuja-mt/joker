FROM python

RUN pip3 install web.py requests

COPY serve.py ./

CMD exec python3 -u serve.py

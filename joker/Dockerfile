FROM python

RUN python3 -m pip install web.py==0.62 requests

COPY serve.py ./

CMD exec python -u serve.py

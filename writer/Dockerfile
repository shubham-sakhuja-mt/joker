FROM python

RUN pip install web.py

COPY jokes.json serve.py ./

CMD exec python -u serve.py

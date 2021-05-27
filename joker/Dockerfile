FROM python

RUN pip --version
RUN pip install web.py requests

COPY serve.py ./

CMD exec python -u serve.py

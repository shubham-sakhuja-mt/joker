FROM 3dpro/webpy

RUN pip install requests

COPY jokes.json serve.py ./

CMD exec python -u serve.py

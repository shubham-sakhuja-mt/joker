FROM utasmile/webpython

RUN pip install requests

COPY jokes.json serve.py ./

CMD exec python -u serve.py

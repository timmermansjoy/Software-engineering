FROM python:3.7.0-alpine3.8

WORKDIR /usr/src/app

COPY . .

RUN python -m pip install --upgrade pip && pip install -e ".[development]" --use-feature=in-tree-build

ENV FLASK_APP=app.py 


CMD python -m flask run
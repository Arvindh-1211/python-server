FROM python:3.12.2-slim as base

WORKDIR /app

RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD python3 -m flask --app server run --host=0.0.0.0

FROM python:3.9-slim

RUN pip install Flask psutil

WORKDIR /app

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
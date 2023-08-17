FROM python:3.9-slim

RUN pip install Flask

RUN pip install Werkzeug

RUN pip install requests

WORKDIR /app

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 8081

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8081"]
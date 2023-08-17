FROM python:3.9-slim

RUN pip install Flask
RUN pip install psutil

WORKDIR /app

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 8082

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8082"]
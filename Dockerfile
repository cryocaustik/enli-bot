FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/
ADD src /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "/app/bot.py" ]
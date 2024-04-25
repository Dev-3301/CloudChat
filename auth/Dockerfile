FROM python:3.9
WORKDIR /auth
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV NAME world

CMD [ "python", "main.py" ]
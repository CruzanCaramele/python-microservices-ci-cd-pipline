FROM python:3.10.6-slim

RUN mkdir -p /app
COPY . main.py  /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]


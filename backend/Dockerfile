FROM python:3

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

EXPOSE 8080

COPY . .

CMD ["python", "./__init__.py"]

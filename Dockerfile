FROM tiangolo/uvicorn-gunicorn:python3.9

RUN mkdir /project

WORKDIR /project

COPY requirements.txt /project

RUN pip install -r requirements.txt

COPY . /project

EXPOSE 8000

CMD ["python", "start.py"]
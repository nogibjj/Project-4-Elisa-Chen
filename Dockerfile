FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /code

COPY . ./

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["python", "./main.py"]
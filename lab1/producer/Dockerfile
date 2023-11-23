FROM python:3.8
COPY requirements.txt ./requirements.txt
WORKDIR .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "./producer.py"]

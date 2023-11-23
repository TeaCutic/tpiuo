FROM python:3.8

ADD producer.py ./producer.py
ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
CMD [ "python", "./producer.py"]

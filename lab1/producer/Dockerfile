FROM python:3.8
RUN ls -al
COPY requirements.txt /requirements.txt
WORKDIR .
RUN pip install -r requirements.txt
RUN ls -al
COPY . .
CMD [ "python", "./producer.py"]

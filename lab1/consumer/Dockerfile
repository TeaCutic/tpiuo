FROM python:3.8
ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ADD consumer.py ./consumer.py
CMD [ "python", "./consumer.py"]
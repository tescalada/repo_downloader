FROM python:3

ADD main.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

VOLUME /Devel

CMD [ "python", "./main.py" ]
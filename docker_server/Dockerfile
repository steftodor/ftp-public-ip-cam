FROM python:3

ADD upload-script.py /
ADD failed_capture.jpg /

RUN pip install requests

CMD [ "python","-u", "./upload-script.py" ]
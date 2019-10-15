FROM debian:jessie-slim

RUN apt-get update                                                                                                                                                                                       
RUN apt-get install -y --fix-missing \
    python3 \
    python3-pip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN mkdir /code
WORKDIR /code    

COPY . /code
RUN pip3 install -r requirements.txt
CMD gunicorn -t 200 --workers=50 -b 0.0.0.0:$PORT src.app:app --log-level=debug
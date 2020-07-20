# from elasticsearch:7.8.0
FROM ubuntu:14.04

RUN apt-get --fix-missing update --fix-missing
RUN apt-get -yq install python-dev python-pip nginx tesseract-ocr imagemagick libyaml-dev

COPY legisletters /legisletters
COPY default /etc/nginx/sites-available/default
COPY elasticsearch.yml ./elasticsearch.yml

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  apt-transport-https \
  wget -y
RUN pip install -r /legisletters/requirements.txt
# RUN plugin install elasticsearch/elasticsearch-mapper-attachments/2.5.0

FROM python:3.7

WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt
RUN mkdir /entrypoint

COPY wait_for_kafka.sh /entrypoint/wait_for_kafka.sh
COPY wait_for_it.sh /entrypoint/wait_for_it.sh

RUN ["chmod", "+x", "/entrypoint/wait_for_kafka.sh"]
RUN ["chmod", "+x", "/entrypoint/wait_for_it.sh"]

ENTRYPOINT ["/entrypoint/wait_for_kafka.sh"]


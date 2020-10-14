FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

RUN mkdir /entrypoint

COPY wait_for_kafka.sh /entrypoint/wait_for_kafka.sh
COPY wait_for_it.sh /entrypoint/wait_for_it.sh

RUN ["chmod", "+x", "/entrypoint/wait_for_kafka.sh"]
RUN ["chmod", "+x", "/entrypoint/wait_for_it.sh"]

ENTRYPOINT ["/entrypoint/wait_for_kafka.sh"]


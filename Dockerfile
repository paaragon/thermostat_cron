FROM python:3.7
RUN apt-get update && apt-get -y install cron vim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY crontab /etc/cron.d/crontab
COPY src/main.py /app/main.py
COPY src/temp_service.py /app/temp_service.py
COPY src/db.py /app/db.py

RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

# run crond as main process of container

CMD printenv > /etc/environment && cron -f

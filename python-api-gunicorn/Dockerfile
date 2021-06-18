FROM ubuntu:18.04
RUN apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip \
    && apt-get install -y sudo
RUN python3 -m pip install pip --upgrade
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["gunicorn", "main:app"]
CMD ["-c", "gunicorn_setting.py"]

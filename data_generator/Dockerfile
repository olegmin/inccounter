FROM python:3.7.3

ADD requirements.txt .

RUN pip3 install --upgrade pip && \
    pip3 install --trusted-host pypi.python.org -r requirements.txt && \
    rm -f requirements.txt

ADD ./appcode /app

WORKDIR /app

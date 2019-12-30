FROM python:3.7.3

ADD requirements.txt .
RUN pip3 install --upgrade pip && \
    pip3 install --trusted-host pypi.python.org -r requirements.txt && \
    rm -f requirements.txt

ADD ./code /app

WORKDIR /app

CMD ["python3", "main.py"]

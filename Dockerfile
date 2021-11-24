FROM python:3.8-slim

ENV LAC_HOST=''
ENV LAC_PORT=''

COPY ./sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y libgomp1
RUN pip install lac Flask gevent --no-cache-dir -i https://mirror.baidu.com/pypi/simple

COPY ./main.py /app/
WORKDIR /app

CMD [ "python", "main.py" ]
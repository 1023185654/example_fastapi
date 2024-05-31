FROM 

WORKDIR /app

RUN sed -i s/deb.debian.org/mirrors.aliyun.com/g /etc/apt/sources.list && \
    sed -i s/security.debian.org/mirrors.aliyun.com/g /etc/apt/sources.list

RUN pip install --no-cache-dir --upgrade pip -i https://pypi.mirrors.ustc.edu.cn/simple/


COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && rm -f requirements.txt

ADD . /app

ENV PYTHONPATH=.

EXPOSE 9000

CMD ["/bin/sh", "entry.sh"]
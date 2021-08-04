FROM python

WORKDIR /usr/src/app

RUN pip install flask
RUN pip install mysql

COPY app ./

CMD ["flask", "run", "--host=0.0.0.0"]

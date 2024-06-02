FROM python:3.10.11-alpine

RUN apk add --no-cache git
#RUN git clone 
RUN mv api-sgpa /usr/src/app

WORKDIR /usr/src/app

#COPY requirements.txt /usr/src/app/
RUN python3 -m pip install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

#COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "app.py"]
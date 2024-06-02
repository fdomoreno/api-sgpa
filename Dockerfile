FROM python:3.10.11-alpine

RUN apk add --no-cache git
#RUN git clone https://luis.moreno.talentotech:mozln6j7rgfahs3pqyq2i2tgdsosfkngv7rtplscgfyrxxhfzowa@dev.azure.com/g1talentotech/Monitoreo%20de%20Emisiones%20de%20Carbono/_git/api_energia
RUN mv api-sgpa /usr/src/app

WORKDIR /usr/src/app

#COPY requirements.txt /usr/src/app/
RUN python3 -m pip install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

#COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "app.py"]
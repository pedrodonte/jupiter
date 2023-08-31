FROM python:3.11

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# zona horaria
ENV TZ=America/Santiago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && dpkg-reconfigure -f noninteractive tzdata


WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app


ENTRYPOINT [ "sh" ]

CMD [ "ejecutar_contenedor.sh" ]


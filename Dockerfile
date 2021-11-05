FROM       python:3.8
LABEL      maintainer="frenk ochse"

WORKDIR    /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

COPY       api.py /app/
RUN        chmod a+x api.py
EXPOSE     5000/tcp

CMD [ "python", "-u", "./api.py" ]

#!/bin/bash

docker build . -t eo2021flaskapi
docker run -p 5000:5000 eo2021flaskapi:latest 

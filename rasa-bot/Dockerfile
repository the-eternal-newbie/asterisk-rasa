FROM python:3.8.7
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# RUN apk add alpine-sdk gcc musl-dev python3-dev libffi-dev openssl-dev cargo jpeg-dev zlib-dev  ffmpeg
# RUN pip install pipenv
# RUN apk add --no-cache gcc musl-dev linux-headers
# COPY Pipfile* .
EXPOSE 5000
EXPOSE 5005
COPY . .
RUN pip install -r requirements.txt
CMD ["flask","run"]
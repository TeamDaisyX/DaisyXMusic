FROM python:3.9.6-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git -y curl ffmpeg python3-pip opus-tools
RUN python3.9 -m pip install -U pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN mkdir /app/
COPY . /app/
WORKDIR /app/
RUN python3.9 -m pip install -U -r requirements.txt
CMD python3.9 -m DaisyXMusic

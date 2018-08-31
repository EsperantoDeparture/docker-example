FROM ubuntu

RUN apt-get clean

RUN rm -rf /var/lib/apt/lists/*

RUN apt-get clean

RUN apt-get update 

# RUN apt-get upgrade

RUN apt-get install -y curl apt-transport-https build-essential bzip2 curl git vim

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

RUN apt-get install -y --no-install-recommends nginx

RUN rm /etc/nginx/sites-enabled/default

RUN apt-get clean

CMD nginx -g "daemon off;"
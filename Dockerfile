FROM ubuntu:16.04

MAINTAINER esperantodeparture

WORKDIR /var/www/html

# This installs apahe, php and libapache2-mod-php. The latter
# enables apache integrates apache with php.
RUN apt-get update && apt-get install -y php libapache2-mod-php apache2

# The port 80 is now accessible outside the container
EXPOSE 80

# Changing the owner of the source code of dokuwiki fixes the
# permision error that happens when dokuwiki tries to create new
# files
COPY --chown=www-data:www-data ./src .

# This will delete the default apache static page, allowing index.php
# to be loaded instead
RUN rm index.html

# This forces the apache to run in the foreground, so the container
# won't close after running.
CMD apache2ctl -D FOREGROUND
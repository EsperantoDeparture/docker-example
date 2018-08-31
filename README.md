# Docker example

This is an example of how to run dokuwiki with docker (or docker-compose).
You can run dokuwiki using just "docker-compose up", that'll start a container
with apache and php. You can also run dokuwiki manually:

$ docker build -t dokuwiki .
$ docker run -d -p 80:08 dokuwiki

The file named docker-compose.yml.old contains a different setup, that
creates two containers, one with nginx and other with php7-fpm used to
run dokuwiki.
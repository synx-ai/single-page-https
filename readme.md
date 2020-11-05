# Single HTTPS enabled page serve using Python
[![Build Status](https://travis-ci.com/synx-ai/single-page-https.svg?branch=master)](https://travis-ci.com/synx-ai/single-page-https)

The main purpuse of this project is to provide a simplistic way with a minimal installation to serve static content for microservices reporting and content testing. **Not intended for production**.


### Pre-requistes

- Clone the contents of this repo in `/home/www` or change **WorkingDirectory** in `py-serve.service`.


### Install let's encrypt certbot

For SSL support, install and configure certbot.

```shell
snap install core; sudo snap refresh core
snap install --classic certbot
certbot certonly --standalone
```


### Install service

To daemonize the server (and add reloading support on system reboot), add the service template to **Ubuntu** services. Change according with your OS.

```shell
cp py-serve.service /lib/systemd/system/pyserve.service
systemctl daemon-reload
service pyserve stop
service pyserve start
```

Change default certfile and keyfile paths on `server.py` or specify them as parameters.

Install hooks to reload server on cert updates:

```shell
sh -c 'printf "#!/bin/sh\nservice pyserve stop\n" > /etc/letsencrypt/renewal-hooks/pre/pyserve.sh'
sh -c 'printf "#!/bin/sh\nservice pyserve start\n" > /etc/letsencrypt/renewal-hooks/post/pyserve.sh'
chmod 755 /etc/letsencrypt/renewal-hooks/pre/pyserve.sh
chmod 755 /etc/letsencrypt/renewal-hooks/post/pyserve.sh
```


### Usage

```
usage: server.py [-h] [-p PORT] [-a ADDRESS] [-c CERTFILE] [-k KEYFILE]

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Server port for listening requests
  -a ADDRESS, --address ADDRESS
                        Server address
  -c CERTFILE, --certfile CERTFILE
                        SSL certificate
  -k KEYFILE, --keyfile KEYFILE
                        SSL Keyfile
```


### Logs

Use system logs to review status and logs.

For status:
```shell
systemctl -l status pyserve
```

For logs:
```shell
journalctl -u pyserve.service -e
```


### Author

Carlos Rivera ([@carlos_gif](https://twitter.com/carlos_gif))

# Single HTTPS enabled page serve using Python

### Pre-requistes

- Clone the contents of this repo in `/home/www` or change **WorkingDirectory** in `py-serve.service`.


### Install let's encrypt certbot

```shell
snap install core; sudo snap refresh core
snap install --classic certbot
certbot certonly --standalone
```


### Install service

```shell
cp py-serve.service /lib/systemd/system/pyserve.service
systemctl daemon-reload
service pyserve stop
service pyserve start
```

Install hooks to reload server on cert updates

```shell
sh -c 'printf "#!/bin/sh\nservice pyserve stop\n" > /etc/letsencrypt/renewal-hooks/pre/pyserve.sh'
sh -c 'printf "#!/bin/sh\nservice pyserve start\n" > /etc/letsencrypt/renewal-hooks/post/pyserve.sh'
chmod 755 /etc/letsencrypt/renewal-hooks/pre/pyserve.sh
chmod 755 /etc/letsencrypt/renewal-hooks/post/pyserve.sh
```

### Author

Carlos Rivera ([@carlos_gif](https://twitter.com/carlos_gif))

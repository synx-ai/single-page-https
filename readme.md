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


### MIT License

Copyright 2020

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

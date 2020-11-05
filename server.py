import sys
import getopt
import http.server
import ssl
import argparse
from datetime import datetime


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--port", type=int,
                        help="Server port for listening requests",
                        default=443)
    parser.add_argument("-a", "--address", type=str,
                        help="Server address",
                        default='0.0.0.0')
    parser.add_argument("-c", "--certfile", type=str,
                        help="SSL certificate",
                        default='/etc/letsencrypt/live/niko.kf.synx.io/fullchain.pem')
    parser.add_argument("-k", "--keyfile", type=str,
                        help="SSL Keyfile",
                        default='/etc/letsencrypt/live/niko.kf.synx.io/privkey.pem')

    args = parser.parse_args()

    print(f'[{str(datetime.now())}] - Server starting on \'{args.address}:{args.port}\'')

    server_address = (args.address, args.port)
    httpd = http.server.HTTPServer(
        server_address, http.server.SimpleHTTPRequestHandler)

    # assume production
    if args.port == 443:
        print(f'[{str(datetime.now())}] - Server certfile: {args.certfile}')
        print(f'[{str(datetime.now())}] - Server keyfile:  {args.keyfile}')

        httpd.socket = ssl.wrap_socket(httpd.socket,
                                       server_side=True,
                                       certfile=args.certfile,
                                       keyfile=args.keyfile,
                                       ssl_version=ssl.PROTOCOL_TLS)

    print(f'[{str(datetime.now())}] - Listening for requests...')

    httpd.serve_forever()


if __name__ == '__main__':
    main()

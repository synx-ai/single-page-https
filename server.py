import sys
import getopt
import http.server
import ssl

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "p:", ["port="])

        for opt, arg in opts:
            if opt in ("-p", "--port"):
                port = int(arg)

    except getopt.GetoptError:
        port = 443

    server_address = ('0.0.0.0', port)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

    # assume production
    if port == 443:
        httpd.socket = ssl.wrap_socket(httpd.socket,
                                       server_side=True,
                                       certfile='/etc/letsencrypt/live/niko.kf.synx.io/fullchain.pem',
                                       keyfile='/etc/letsencrypt/live/niko.kf.synx.io/privkey.pem',
                                       ssl_version=ssl.PROTOCOL_TLS)
    httpd.serve_forever()


if __name__ == '__main__':
    main(sys.argv[1:])

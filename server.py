import http.server
import ssl

server_address = ('0.0.0.0', 443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile='/etc/letsencrypt/live/niko.kf.synx.io/fullchain.pem',
                               keyfile='/etc/letsencrypt/live/niko.kf.synx.io/privkey.pem',
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()

import requests
import server
from nose.tools import assert_true, assert_raises


def test_request_response():
    # Send a request to the server and store the response.
    response = requests.get('http://localhost:8443/')

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)


def test_import_server_init():
    resp = server.init()

    assert_true(resp == None)

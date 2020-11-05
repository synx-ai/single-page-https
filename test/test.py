from nose.tools import assert_true
import requests


def test_request_response():
    # Send a request to the server and store the response.
    response = requests.get('https://localhost:8843/')

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)

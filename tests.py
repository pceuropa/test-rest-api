"""
File: tests.py
Authors: Rafal Marguzewicz
Emails: info@pceuropa.net
Description: tests - pytest
"""

from json import load
from urllib.request import urlopen, Request
from urllib import error

host = f"https://blockchain.info/rawblock/"
endpoint = '0000000000000bae09a7a393a8acded75aa67e46cb81f7acaa5ad94f9eacd103'


def headers():
    """
    Posibility adding authorization token to header of  request
    """
    return {'Authorization': 'token_secure'}


def request(endpoint_url: str=''):
    return Request(f"{host}/{endpoint_url}", headers=headers())


def test_endpoint_200():
    """
    Response 200
    """
    req = request(f"{endpoint}")
    assert 200 == urlopen(req).getcode()


def test_endpoint_data_in_json():
    """
    Response json
    """
    json_data = load(urlopen(f"{host}/0000000000000bae09a7a393a8acded75aa67e46cb81f7acaa5ad94f9eacd103"))
    assert json_data['hash'] == endpoint


def test_endpoint_500():
    """
    Reponse 404
    """
    req = request(f"endpoint_with_404")

    try:
        urlopen(req).getcode()
    except error.HTTPError as e:
        assert e.code == 500  # or 404

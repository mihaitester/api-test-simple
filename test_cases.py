import pytest
import requests

def test_get_200():
    """
    """
    r = requests.get('https://urlhaus-api.abuse.ch/v1/urls/recent/')
    assert r.status_code == 200



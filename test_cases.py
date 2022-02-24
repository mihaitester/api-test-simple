import pytest
import requests

"""
File containing testcases for API https://urlhaus.abuse.ch/api/
INFO: https://urlhaus-api.abuse.ch/#urls-recent
"""

def test_https_get_recent_code_200(url="https://urlhaus-api.abuse.ch/v1/urls/recent/"):
    r = requests.get(url)
    assert r.status_code == 200

def test_http_get_recent_code_404(url="http://urlhaus-api.abuse.ch/v1/urls/recent/"):
    r = requests.get(url)
    assert r.status_code == 404

def test_get_recent_limit_3_code_200(url="https://urlhaus-api.abuse.ch/v1/payloads/recent/limit/3/"):
    r = requests.get(url)
    print(r.json())
    assert r.status_code == 200


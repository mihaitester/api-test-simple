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
    # todo: maybe mark negative tests somehow, or include them in a different test suite
    r = requests.get(url)
    assert r.status_code == 404

def test_get_recent_limit_3_code_200(url="https://urlhaus-api.abuse.ch/v1/payloads/recent/limit/3/"):
    r = requests.get(url)
    assert r.status_code == 200

def test_get_recent_limit_3_virustotal_result(url="https://urlhaus-api.abuse.ch/v1/payloads/recent/limit/3/"):
    r = requests.get(url)
    payloads = [ x for x in r.json()["payloads"] ]
    toxicity = []
    for y in payloads:
        virustotal = y["virustotal"]
        if None != virustotal:
            result = y["virustotal"]["result"]
            link = y["virustotal"]["result"]
            toxicity += [ { "result": result, "link": link } ]
    assert len(payloads) == len(toxicity), "Not all recent malware was tested on virustotal"

# todo: add POST tests, will need to upload a malware file, and will need to create a user account with this website

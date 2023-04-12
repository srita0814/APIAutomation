import pytest
import requests

from requests import ConnectTimeout, HTTPError


class TestRequest:
    @pytest.mark.get
    def test_response(self):
        url = "http://httpbin.org/get"
        data = {'key1': 'value1', 'key2': ['value2', 'value3']}
        r = requests.request('get', url, params=data)
        print(r.url)
        print(r.status_code)
        print(r.headers)
        # print(r.headers['Content-Type'])
        print(r.encoding)
        print(r.apparent_encoding)
        # print(r.content)
        # print(r.text)
        # print(r.json())
        print(r.cookies)
        print(r.request.headers)

    def test_response2(self):
        url = 'http://github.com/'
        response_redirect = requests.get(url)
        response_not_redirect = requests.get(url, allow_redirects=False)
        print(response_redirect.url)
        print(response_redirect.status_code)
        print(response_redirect.history)
        print(response_not_redirect.url)
        print(response_not_redirect.status_code)
        print(response_not_redirect.history)

    @pytest.mark.xfail(raises=ConnectTimeout, reason="ConnectTimeoutError")
    def test_response3(self):
        url = 'http://httpbin.org/get'
        r = requests.request('get', url, timeout=0.001)
        r.raise_for_status()

    @pytest.mark.xfail(raises=HTTPError, reason="404 Not Found")
    def test_response4(self):
        url = 'http://httpbin.org/status/404'
        r = requests.request('get', url)
        r.raise_for_status()

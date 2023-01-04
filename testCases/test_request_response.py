import pytest
import requests
import json

from requests import ConnectTimeout, HTTPError


class TestRequest:
    @pytest.mark.get
    def test_response(self):
        url = "http://httpbin.org/get"
        data = {'key1': 'value1', 'key2': ['value2', 'value3']}
        response = requests.request('get', url, params=data)
        # print(response.request)
        # print(response.url)
        # print(response.status_code)
        # print(response.headers)
        # print(response.headers['Content-Type'])
        # print(response.encoding)
        # print(response.apparent_encoding)
        # print(response.content)
        # print(response.text)
        # print(response.json())
        print(response.cookies)

    def test_response2(self):
        url = 'http://httpbin.org/get'
        data = {'key1': 'value1', 'key2': 'value2'}
        # 将 字典类型 转换为 JSON 对象
        json_str = json.dumps(data)
        print('Original data', repr(data))
        print('Json object', json_str)
        # 将 JSON 对象转换为 字典类型
        data2 = json.loads(json_str)
        print('data2 is', data2)

    def test_response2(self):
        url = 'http://httpbin.org/cookies'
        cookies_set = {'cookies_are': 'testing'}
        response2 = requests.get(url, cookies=cookies_set)
        print(response2.cookies)

    def test_response3(self):
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
    def test_response4(self):
        url = 'http://httpbin.org/get'
        response4 = requests.request('get', url, timeout=0.001)
        response4.raise_for_status()

    @pytest.mark.xfail(raises=HTTPError, reason="404 Not Found")
    def test_response5(self):
        url = 'http://httpbin.org/status/404'
        response5 = requests.request('get', url)
        response5.raise_for_status()

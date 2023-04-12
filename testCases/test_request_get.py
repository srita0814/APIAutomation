import pytest
import requests


class TestRequest:

    @pytest.mark.get
    def test_get_method_without_args(self):
        url = "http://httpbin.org/get"
        r = requests.request('get', url)
        print(r.request.headers)
        print(r.url)
        # print('The response of request method without args:' + r.text)

    @pytest.mark.get
    def test_get_method_with_args(self):
        url = "http://httpbin.org/get"
        data = {'key1': 'value1', 'key2': ['value2', 'value3']}
        headers = {
            'accept-language': 'en-US,en;q=0.9'
        }
        cookies = {
            'token': 'ABCDEF'
        }
        r = requests.request('get', url, params=data, headers=headers, cookies=cookies)
        print(r.request.headers)
        print(r.url)
        # print('The response of request method with args:' + r.text)



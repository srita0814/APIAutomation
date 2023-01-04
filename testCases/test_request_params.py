import pytest
import requests


class TestRequest:
    @pytest.mark.get
    def test_get_params(self):
        url = "http://httpbin.org/get"
        data = {'key1': 'value1', 'key2': ['value2', 'value3']}
        response = requests.request('get', url, params=data)
        print(response.url)



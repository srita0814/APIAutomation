import pytest
import requests


class TestRequest:

    @pytest.mark.post
    def test_post_body(self):
        url = "http://httpbin.org/post"
        data = {'key1': 'value1', 'key2': 'value2'}
        response = requests.post(url, data)
        response1 = requests.post(url, data=data)
        response2 = requests.post(url, json=data)
        print(response.text)
        print(response1.text)
        print(response2.text)

    @pytest.mark.post
    def test_post_body2(self):
        url = "http://httpbin.org/post"
        data = "test"
        response3 = requests.post(url, data=data)
        response4 = requests.post(url, json=data)
        print(response3.text)
        print(response4.text)

    @pytest.mark.post
    def test_post_body3(self):
        url = "http://httpbin.org/post"
        upload_files = {'file': open('test_fileupload.txt', 'rb')}
        response5 = requests.post(url, files=upload_files)
        print(response5.text)

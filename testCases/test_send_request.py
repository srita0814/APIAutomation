import pytest
import requests


class TestRequest:
    @pytest.mark.get
    def test_get_method(self):
        url = "http://httpbin.org/get"
        r = requests.get(url)
        print(r.text)

    @pytest.mark.post
    def test_post_method(self):
        url = "http://httpbin.org/post"
        r = requests.post(url)
        print('The response of post method:' + r.text)

    @pytest.mark.put
    def test_put_method(self):
        url = "http://httpbin.org/put"
        r = requests.put(url)
        print('The response of put method:' + r.text)

    @pytest.mark.delete
    def test_delete_method(self):
        url = "http://httpbin.org/delete"
        r = requests.delete(url)
        print('The response of delete method:' + r.text)

    @pytest.mark.patch
    def test_patch_method(self):
        url = "http://httpbin.org/patch"
        r = requests.patch(url)
        print('The response of patch method:' + r.text)

    @pytest.mark.request
    def test_request_method(self):
        url = "http://httpbin.org/get"
        r = requests.request('get', url)
        print('The response of request method:' + r.text)


import pytest
import requests


class TestRequest:
    @pytest.mark.get
    def test_get_method(self):
        url = "http://httpbin.org/get"
        response = requests.get(url)
        print('The response of get method:' + response.text)

    @pytest.mark.post
    def test_post_method(self):
        url = "http://httpbin.org/post"
        response = requests.post(url)
        print('The response of post method:' + response.text)

    @pytest.mark.put
    def test_put_method(self):
        url = "http://httpbin.org/put"
        response = requests.put(url)
        print('The response of put method:' + response.text)

    @pytest.mark.delete
    def test_delete_method(self):
        url = "http://httpbin.org/delete"
        response = requests.delete(url)
        print('The response of delete method:' + response.text)

    @pytest.mark.patch
    def test_patch_method(self):
        url = "http://httpbin.org/patch"
        response = requests.patch(url)
        print('The response of patch method:' + response.text)

    # @pytest.mark.request
    # def test_request_method(self):
    #     url = "http://httpbin.org/get"
    #     response = requests.request('get', url)
    #     print('The response of request method:' + response.text)

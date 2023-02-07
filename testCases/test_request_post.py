import pytest
import requests


class TestRequest:

    @pytest.mark.post
    def test_post_body_data(self):
        url = "http://httpbin.org/post"
        dict_data = {'key1': 'value1', 'key2': 'value2'}
        str_data = "test string data"
        list_of_tuple_data = [('key1', 'value1'), ('key2', 'value2')]
        # data作为参数，传入字典，字符串，元组组成的列表
        r = requests.request('post', url, data=dict_data)
        r2 = requests.request('post', url, data=str_data)
        r3 = requests.request('post', url, data=list_of_tuple_data)
        print(r.text)
        print(r2.text)
        print(r3.text)

    @pytest.mark.post
    def test_post_body_json(self):
        url = "http://httpbin.org/post"
        dict_data = {'key1': 'value1', 'key2': 'value2'}
        str_data = "test string data"
        list_of_tuple_data = [('key1', 'value1'), ('key2', 'value2')]
        # json作为参数，传入字典，字符串，元组组成的列表
        r = requests.request('post', url, json=dict_data)
        r2 = requests.request('post', url, json=str_data)
        r3 = requests.request('post', url, json=list_of_tuple_data)
        print(r.text)
        print(r2.text)
        print(r3.text)

    # 文件上传
    @pytest.mark.post
    def test_post_upload_file(self):
        url = "http://httpbin.org/post"
        upload_files = {'file': open('test_file_upload.txt', 'rb')}
        r = requests.request('post', url, files=upload_files)
        print(r.text)

    # 文件下载
    # @pytest.mark.post
    # def test_post_download_file(self):
    #     url = "http://www.comm100.com"
    #     r = requests.request('get', url)
    #     with open('test_file_download.html', 'wb') as f:
    #         f.write(r.content)

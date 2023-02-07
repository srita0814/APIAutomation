import json


class TestRequest:

    def test_func_dumps_loads(self):
        dict_data = {'key1': 'value1', 'key2': 'value2'}
        # 将字典类型转换为JSON格式的字符串类型
        str_data = json.dumps(dict_data)
        print(type(str_data))
        print(str_data)
        # 将JSON格式的字符串类型转换为字典类型
        json_data = json.loads(str_data)
        print(type(json_data))
        print(json_data)

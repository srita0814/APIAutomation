
class TestRequest:
    # 判断方法或者函数的返回值是否为真
    def test_assert1(self):
        a = 1
        assert a

    def test_assert2(self):
        a = 0
        assert not a

    # 判断包含或不包含
    def test_assert3(self):
        s = 'hello'
        assert 'h' in s

    def test_assert4(self):
        s = 'hello'
        assert 'y' not in s

    # 比较大小与是否相等
    def test_assert5(self):
        a = 3
        assert a == 3

    def test_assert6(self):
        a = 4
        assert a != 3

    # 判断类型
    def test_assert7(self):
        a = 4
        assert isinstance(a, int)



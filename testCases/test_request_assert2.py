import pytest


class TestRequest:

    # 指定断言失败消息:
    def test_assert1(self):
        a = 3
        assert a == 50, f"判断a为50，当前a的值为{a}"

    # 预期内异常报错断言
    def test_assert2(self):
        1 / 0

    @pytest.mark.xfail(raises=ZeroDivisionError)
    def test_assert3(self):
        with pytest.raises(ZeroDivisionError) as e:
            1 / 0
        print(e.traceback)
        assert e.type == ZeroDivisionError
        assert 'division by zero' in str(e.value)

    # 非预期异常报错断言
    @pytest.mark.parametrize('x')
    def division(self, x):
        if x == 0:
            raise ValueError('division by zero raised')
        if isinstance(x, str):
            raise TypeError('value is not string')
        return 100/x

    @pytest.mark.xfail(raises=ValueError)
    def test_match_01(self):
        with pytest.raises(ValueError, match=r'.* zero .*') as e:
            self.division(0)
        assert e.type == ValueError
        assert "division by zero raised" in str(e.value)

    @pytest.mark.xfail(raises=TypeError)
    def test_match_02(self):
        with pytest.raises(TypeError, match='value is not string') as e:
            self.division("string")
        assert e.type == TypeError
        assert "value is not string" in str(e.value)




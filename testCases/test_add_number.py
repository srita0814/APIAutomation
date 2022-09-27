import pytest
import yaml

read_file = yaml.safe_load(open("test_add_number.yml"))
case_names = []
params = []
for case_data in read_file['addNumberTest']:
    case_names.append(case_data['case'])
    params.append(case_data['numbers'])


def add(x, y):
    return x + y


class TestAddNumber:
    @pytest.mark.smoke
    @pytest.mark.add
    @pytest.mark.parametrize('x, y', [params[0]], ids=[case_names[0]])
    def test_add_positive_number(self, x, y):
        #print(x, y)
        assert add(x, y) == 3

    @pytest.mark.smoke
    @pytest.mark.add
    @pytest.mark.parametrize('x, y', [params[1]], ids=[case_names[1]])
    def test_add_negative_number(self, x, y):
        #print(x, y)
        assert add(x, y) == -3

    @pytest.mark.smoke
    @pytest.mark.add
    @pytest.mark.parametrize('x, y', [params[2]], ids=[case_names[2]])
    def test_add_big_number(self, x, y):
        #print(x, y)
        assert add(x, y) == 1000000000

    @pytest.mark.smoke
    @pytest.mark.add
    @pytest.mark.parametrize('x, y', [params[3]], ids=[case_names[3]])
    def test_add_zero_number(self, x, y):
        #print(x, y)
        assert add(x, y) == 1

    @pytest.mark.smoke
    @pytest.mark.add
    @pytest.mark.xfail(raises=TypeError, reason="illegal input")
    @pytest.mark.parametrize('x, y', [params[4]], ids=[case_names[4]])
    def test_add_illegal_number(self, x, y):
        #print(x, y)
        assert add(x, y) == "ab"
import pytest
import yaml



class TestData:

    @pytest.mark.parametrize("a, b", [(1,1), (2, 2), (3, 3)])
    def test_data(self, a, b):
        print(f"a + b = {a + b}")

    @pytest.mark.parametrize(["c","d"], yaml.safe_load(open("./data.yaml")))
    def test_yaml_data(self, c, d):
        print(f"c + d = {c + d}")

if __name__ == '__main__':
    pytest.main(["-v", "-s"])


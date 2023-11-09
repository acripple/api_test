import pytest
import requests

from common.read_data import read_casedata, read_yaml


class TestSamle:
    def test_user(self):
        url = "http://127.0.0.1:5000/users"
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        res = requests.get(url=url, headers=headers)
        print("登录成功: " + res.text)

    @pytest.mark.parametrize("mima", read_casedata("../test_api/test_user.yaml"))
    def test_register(self, mima):
        # print("dasda", mima["request"]["headers"])
        method = mima["request"]["method"]
        url = mima["request"]["url"]
        headers = mima["request"]["headers"]
        data = mima["request"]["json"]
        data["password"] = "guoshjie"
        print(data)
        # for key,value in data.items():
        #     print(key,value)
        #     data[key] = read_yaml(key)
        #     print(data)
        res = requests.post(url, json=data, headers=headers)
        print("注册成功: " + res.text)

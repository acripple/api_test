import yaml
import os

lujing = "C:\\Users\\31752\\PycharmProjects\\flaskProject\\test_api\\file.yaml"


def write_yaml(data):
    with open(lujing, encoding='utf-8',
              mode='a+') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


def read_yaml(key):
    with open("C:\\Users\\31752\\PycharmProjects\\flaskProject\\test_api\\file.yaml", encoding='utf-8',
              mode='r') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value[key]


def clear_yaml():
    with open(lujing, encoding='utf-8',
              mode='w') as f:
        f.truncate()


def read_casedata(path):
    with open(path, encoding='utf-8',
              mode='r') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value

if __name__ == '__main__':
    print(read_casedata("../test_api/file.yaml"))
    print(read_yaml("password"))

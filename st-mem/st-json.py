# _*_ coding: utf-8 _*_
# @Time : 2022/4/1 下午11:01 
# @Author : wangyefei
# @File : st-json.py
import json
from datetime import datetime
from typing import Any


def test_json_pretty_output():
    fp = open('output.json', mode='a')
    alphabet = {k: chr(k + 97) for k in range(26)}
    json.dump(alphabet, fp, sort_keys=True, indent=4)


class CustomEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):
            return int(o.timestamp())
        if isinstance(o, set):
            return list(o)
        return super().default(self)


if __name__ == '__main__':
    user_data = dict(id=1, name="nacy", ts=datetime.now(), hobby={'read', 'writting'})
    try:
        print(json.dumps(user_data))
    except Exception as e:
        # import traceback
        # traceback.print_exc()
        print(json.dumps(user_data, cls=CustomEncoder))

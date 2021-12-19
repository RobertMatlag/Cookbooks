import json
from collections import OrderedDict


if __name__ == "__main__":
    od = OrderedDict()

    od["foo"] = 1
    od["bar"] = 2
    od["spam"] = 3
    od["eggs"] = 4
    od["spam"] = 3

    for key, value in od.items():
        print(key, value)

    print(json.dumps(od))

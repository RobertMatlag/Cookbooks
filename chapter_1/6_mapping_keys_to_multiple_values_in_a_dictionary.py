from collections import defaultdict

# 1
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
d["b"].append(4)


# 2 tak nie robić, init default value przy każdym appendzie

d2 = {}
d2.setdefault("a", []).append(1)
print(d2)
d2.setdefault("a", []).append(2)
print(d2)
d2.setdefault("b", []).append(4)
print(d2)


if __name__ == "__main__":
    print(d)

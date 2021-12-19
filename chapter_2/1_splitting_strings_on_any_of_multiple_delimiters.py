import re

line = "asdf fjdk; afed, fjek,asdf,      foo"

if __name__ == "__main__":
    print(re.split(r"[;,\s]\s*", line))

    # 2 jak sie grupuje, to re.split() wyrzuca też w grupach delimiter
    fields = re.split(r"(;|,|\s)\s*", line)
    print(fields)

    # 3
    values = fields[::2]
    delimiters = fields[1::2] + [""]
    print(values)
    print(delimiters)

    print("".join(v + d for v, d in zip(values, delimiters)))

    # 4 non capturing group ?;
    print(re.split(r'(?:,|;|\s)\s*', line))

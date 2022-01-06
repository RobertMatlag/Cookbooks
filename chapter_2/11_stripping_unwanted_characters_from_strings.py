s = "     hello world \n"
t = "-----hello====="
u = "     hello          world \n"

if __name__ == "__main__":
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())

    # 2
    print(t.lstrip("-"))
    print(t.strip("=-"))

    # 3
    print(u.strip())
    print(u.replace(" ", ""))

    import re

    print(re.sub(r"\s+", " ", u).strip())

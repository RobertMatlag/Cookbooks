s = "{name} has {n} messages"


class Info:
    def __init__(self, name, n) -> None:
        self.n = n
        self.name = name


class subsafe(dict):
    def __missing__(self, key):
        return f"{{ {key} }}"


if __name__ == "__main__":
    name = "Guido"
    n = 37

    print(s.format(name=name, n=n))
    print(f"{name} has {n} messages")

    print(s.format_map(vars()))

    a = Info("Guido", 37)
    print(s.format_map(vars(a)))

    # 2
    del n
    print(s.format_map(subsafe(vars())))

    import sys

    def sub(text):
        print(sys._getframe(1).f_locals)
        return text.format_map(subsafe(sys._getframe(1).f_locals))

    name = "Robert"
    n = 37

    print(sub(s))

    import string

    template = string.Template("$name has $n messages")
    print(vars())
    print(template.substitute(name=name, n=n))
    print(template.substitute(vars()))



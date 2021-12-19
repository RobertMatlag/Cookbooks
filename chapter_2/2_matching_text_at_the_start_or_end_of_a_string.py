from urllib.request import urlopen

filename = "spam.txt"
url = "http://www.python.org"
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]

# 3
def read_data(name):
    # tu musi być tupla w argumencie, przy innym iterable wywali błąd
    if name.startswith(("http:", "https:", "ftp:")):
        return urlopen(name).read()
    with open(name) as f:
        return f.read()


if __name__ == "__main__":
    print(filename.endswith(".txt"))
    print(filename.startswith("file:"))
    print(url.startswith("http:"))

    # 2
    print([name for name in filenames if name.endswith((".h", ".c"))])
    print(any(name for name in filenames if name.endswith(".py")))

    # 4 można też używać, sliców, ale to mniej czytelne, a także regexów ale to overkill przy takich prostych przypadakch
    import re

    re.match("http:|https:|ftp:", url)

    # 5 elegancko można skracać kod
    if any(name.endswith((".h", ".c")) for name in filenames):
        print("yes, it is")

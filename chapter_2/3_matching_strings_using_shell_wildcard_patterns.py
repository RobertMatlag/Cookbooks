from fnmatch import fnmatch, fnmatchcase

names = ["Dat1.csv", "Dat2.csv", "config.ini", "foo.py"]

if __name__ == "__main__":
    # fnmatch pozwala na stosowanie wildcardów w przeciwieństwie do .startswith()/.endswith()
    print(fnmatch("foo.txt", "*.txt"))
    print(fnmatch("foo.txt", "?oo.txt"))
    print(fnmatch("Dat45.csv", "Dat[0-9]*"))

    print([name for name in names if fnmatch(name, "Dat*.csv")])

    # 2 UWAGA: fnmatch używa zasad case-senstice jak filesytem ,czyli to zalezy od systemu operacyjnego
    # Na Mac'u fnmatch('foo.txt', '*.TXT') da nam False, a na Windowsie True

    # 3 fnmatchcase jest case-sensitive
    print(fnmatchcase("foo.txt", "*.TXT"))  # False

    # 4
    addresses = [
        "5412 N CLARK ST",
        "1060 W ADDISON ST",
        "1039 W GRANVILLE AVE",
        "2122 N CLARK ST",
        "4802 N BROADWAY",
    ]

    print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
    print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

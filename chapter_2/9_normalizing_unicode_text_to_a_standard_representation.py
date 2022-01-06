import unicodedata

s1 = "Spicy Jalape\u00f1o"
s2 = "Spicy Jalapen\u0303o"

if __name__ == "__main__":
    print(s1)
    print(s2)

    print(len(s1) == len(s2))

    # 1
    t1 = unicodedata.normalize("NFC", s1)
    t2 = unicodedata.normalize("NFC", s2)

    print(ascii(t1))
    print(ascii(t2))
    print(t1 == t2)

    # 2
    t1 = unicodedata.normalize("NFD", s1)
    t2 = unicodedata.normalize("NFD", s2)

    print(ascii(t1))
    print(ascii(t2))
    print(t1 == t2)

    # 3
    s3 = "\ufb01"
    t0 = unicodedata.normalize("NFC", s3)
    t1 = unicodedata.normalize("NFKC", s3)
    t2 = unicodedata.normalize("NFKD", s3)
    print(ascii(t0))
    print(ascii(t1))
    print(ascii(t2))

    # 4 mozna spr czy character jest złozony czy nie
    t4 = unicodedata.normalize("NFD", s1)
    print("".join(ele for ele in t4 if not unicodedata.combining(ele)))

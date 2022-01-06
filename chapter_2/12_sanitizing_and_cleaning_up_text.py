s = "pýtĥöñ\fis\tawesome\r\n"

if __name__ == "__main__":
    print(s)
    remap = {
        ord("\f"): " ",
        ord("\t"): " ",
        ord("\r"): None,
    }
    print(s.translate(remap))
    r = s.translate(remap)

    # 2
    import unicodedata
    import sys

    cmb = dict.fromkeys(
        c for c in range(sys.maxunicode) if unicodedata.combining(chr(c))
    )

    a = unicodedata.normalize("NFD", r)
    print(a.translate(cmb))

    # 3
    print(3, unicodedata.normalize("NFD", r).encode("ascii", "ignore").decode("ascii"))
    digit_map = {
        c: ord('0') + unicodedata.digit(chr(c))
        for c in range(sys.maxunicode)
        if unicodedata.category(chr(c)) == "Nd"
    }

    print(len(digit_map))

    x = '\u0661\u0662\u0663'
    print(x.translate(digit_map))

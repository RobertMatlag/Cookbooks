import re

num = re.compile(r"\d+")
if __name__ == "__main__":
    print(num.match("123"))
    print(num.match("\u0661\u0662\u0663"))

    # 2 mozna zapisac w unicodach regex
    arabic = re.compile("[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+")

    # 3 uwaga na specjalne znaki
    pat = re.compile("stra\u00dfe", re.IGNORECASE)
    s = "straße"
    print(pat.match(s))
    print(pat.match(s.upper()))
    print(
        s.upper()
    )  # jak widać, pomimo flagi nie został odnaleziony, ponieważ 'wielka' forma rózni się

import re
from calendar import month_abbr

text = "yeah, but no, but yeah, but no, but yeah"

if __name__ == "__main__":
    print(text)
    text = text.replace("yeah", "yep")
    print(text)

    # 2 using re.sub(), in the second arg is output pattern
    text = "Today is 11/27/2012. PyCon starts 3/13/2013."
    print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))

    # 3 compiling to object
    datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
    print(datepat.sub(r"\3-\1-\2", text))

    # 4 using callback
    def change_date(m):
        mon_name = month_abbr[int(m.group(1))]
        return f"{m.group(2)} {mon_name} {m.group(3)}"

    print(datepat.sub(change_date, text))

    # 5 re.subn() zwraca jeszcze ile razy było zmienione

    newtext, n = datepat.subn(r"\3-\1-\2", text)
    print(newtext, n)

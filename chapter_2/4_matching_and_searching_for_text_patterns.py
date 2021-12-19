text = "yeah, but no, but yeah, but no, but yeah"

if __name__ == "__main__":
    # 1 exact match
    print(text == "yeah")

    # 2 match at start or end
    print(text.startswith("yeah"))
    print(text.endswith("no"))

    # 3 search for location
    print(text.find("no"))

    # 4 using re
    text1 = "11/27/2012"
    text2 = "Nov 27, 2012"

    import re

    if re.match(r"\d+/\d+/\d+", text1):
        print("yes")
    else:
        print("no")

    if re.match(r"\d+/\d+/\d+", text2):
        print("yes")
    else:
        print("no")

    # 5 compile to re object and reuse
    datepat = re.compile(r"\d+/\d+/\d+")
    if datepat.match(text1):
        print("yes")
    else:
        print("no")

    if datepat.match(text2):
        print("yes")
    else:
        print("no")

    # 6 match szuka od początku i zatrzymuje sie na pierwszym znalezionym, do szukania wszystkich jest inna metoda findall()
    text = "Today is 11/27/2012. PyCon starts 3/13/2013."
    print(datepat.findall(text))

    # 7 grouping
    datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
    m = datepat.match("11/27/2012")
    print(m)

    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))

    print(m.groups())

    month, day, year = m.groups()
    print(day, month, year)

    # 8 use in for loop
    text = "Today is 11/27/2012. PyCon starts 3/13/2013."
    print(datepat.findall(text))
    for month, day, year in datepat.findall(text):
        print(f"{month}-{day}-{year}")

    # 9  using finditer
    print("finditer")
    for m in datepat.finditer(text):
        print(m.groups())

    # 10 exact match $
    random_text = "11/27/2012ascvvsa"
    print(datepat.match(random_text))
    datepat = re.compile(r"(\d+)/(\d+)/(\d+)$")
    print(datepat.match(random_text))  # nothing match

    # 11 jest jeszcze findall() z modułu re. Można go używać nawet często, ponieważ ma cachowany pattern. Jednak
    # szybciej jest troche skompilować do obiektu i używać findall() z obiektu szczególnie jak jest dużo porównań

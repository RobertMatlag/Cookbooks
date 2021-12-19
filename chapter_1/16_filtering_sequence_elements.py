mylist = [1, 4, -5, 10, -7, 2, 3, -1]
values = ["1", "2", "-3", "-", "4", "N/A", "5"]


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


addresses = [
    "5412 N CLARK",
    "5148 N CLARK",
    "5800 E 58TH",
    "2122 N CLARK",
    "5645 N RAVENSWOOD",
    "1060 W ADDISON",
    "4801 N BROADWAY",
    "1039 W GRANVILLE",
]


if __name__ == "__main__":
    print([a for a in mylist if a > 0])
    print([a for a in mylist if a < 0])
    # generator expression
    for element in (a for a in mylist if a < 0):
        print(element)

    # 2
    print(values)
    print(list(filter(is_int, values)))

    # 3
    from itertools import compress

    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    more5 = [n > 5 for n in counts]
    print(more5)
    print(list(compress(addresses, more5)))

def drop_first_last(grades):
    first, *middle, last = grades
    return middle


def do_foo(x, y):
    print("foo", x, y)


def do_bar(s):
    print("bar", s)


def my_sum(items):
    head, *tail = items
    return head + my_sum(tail) if tail else head


def run():
    # 1
    grades = list(range(10))
    print(drop_first_last(grades))

    # 2
    record = "Dave", "dave@example.com", "111-222-3333", "444-555-6666"
    name, email, *phone_numbers = record
    print(name)
    print(email)
    print(phone_numbers)

    # 3
    records = [("foo", 1, 2), ("bar", "Hello"), ("foo", 3, 4)]
    for tag, *args in records:
        if tag == "foo":
            do_foo(*args)
        elif tag == "bar":
            do_bar(*args)

    # 4
    line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"
    name, *fields, home_dir, sh = line.split(":")
    print(name)
    print(home_dir)
    print(sh)

    # 5
    data = ["ACME", 50, 123.45, (20, 12, 2021)]
    name, *_, (*_, year) = data  # 😇
    print(name)
    print(year)

    # 6 nie używać tak rekurencji, to tylko przykład do ćwieczeń
    items = [1, 10, 7, 4, 5, 9]
    print(my_sum(items))


if __name__ == "__main__":
    run()

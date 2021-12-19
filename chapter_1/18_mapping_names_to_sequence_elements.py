from collections import namedtuple

Subscriber = namedtuple("Subscriber", ["addr", "joined"])
sub = Subscriber("a@a.pl", "2021-10-19")

Stock = namedtuple("Stock", ["name", "shares", "price"])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


if __name__ == "__main__":
    print(sub)
    print(sub.addr)
    print(sub.joined)

    addr, joined = sub
    print(addr)
    print(joined)

    # 2
    Stock = namedtuple("Stock", ["name", "shares", "price"])

    s = Stock("ACME", 100, 123.45)
    print(s)
    s = s._replace(shares=75)
    print(s)

    # 3
    Stock = namedtuple("Stock", ["name", "shares", "price", "date", "time"])
    stock_prototype = Stock("", 0, 0.0, None, None)

    def dict_to_stock(s):
        return stock_prototype._replace(**s)


    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}

    print(dict_to_stock(a))
    print(dict_to_stock(b))




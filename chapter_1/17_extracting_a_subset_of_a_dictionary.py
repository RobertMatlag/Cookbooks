prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20, "FB": 10.75}
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }

if __name__ == "__main__":
    p1 = {key: value for key, value in prices.items() if value > 200}
    print(p1)

    p2 = {key: value for key, value in prices.items() if key in tech_names}
    print(p2)

    # 2 mozna tak, ale czyściej jest w p1
    p3 = dict((key, value) for key, value in prices.items() if value > 200)
    print(p3)

    # 3
    p4 = {key: prices[key] for key in prices.keys() & tech_names}
    print(p4)

    print(set([1,2,3,4]) & set([2,3,4,5,6]))
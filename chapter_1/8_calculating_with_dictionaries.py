prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "FB": 10.75,
    "AAA": 45.23,
    "ZZZ": 45.23,
}

if __name__ == "__main__":
    print(min(zip(prices.values(), prices.keys())))
    print(max(zip(prices.values(), prices.keys())))
    price_sorted = sorted(zip(prices.values(), prices.keys()))
    print(price_sorted)

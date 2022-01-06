parts = ["Is", "Chicago", "Not", "Chicago?"]

if __name__ == "__main__":
    print(" ".join(parts))
    print(",".join(parts))
    print("".join(parts))

    # 2
    a = "Is Chicago"
    b = "Not Chicago?"
    print(a + " " + b)

    print("{} {}".format(a, b))
    print(f"{a} {b}")

    print(a + " " + b)

    # 3
    a = "Hello" "World"
    print(a)

    """
        łączenie stringów poprzez += jest nieefektywne, ponieważ tworzone są nowe obiekty dla każdej operacji dodawania
    """

    data = ["ACME", 50, 91.1]
    s = ""
    for ele in data:
        s += str(ele)

    print(s)

    """
        szybciej jest zebrać elementy do kolekcji i wykorzystać metode str.join()
        najlepiej stworzyć generator z elementami do łączenia i podać go bezpośrednio w .join()
    """
    print("".join(str(ele) for ele in data))

    # 4
    a, b, c = "a", "b", "c"

    print(a + ":" + b + ":" + c)  # ugly
    print(":".join((a, b, c)))  # still ugly
    print(a, b, c, sep=":")  # jak tylko do wyświetlania to można tak zaczarować

    # 5

    def sample():
        yield "Chicago"
        yield "Is"
        yield "Not"
        yield "Chicago"

    print("".join(sample()))

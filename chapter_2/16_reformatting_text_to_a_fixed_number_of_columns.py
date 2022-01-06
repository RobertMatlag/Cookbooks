import os
import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

if __name__ == "__main__":
    print(textwrap.fill(s, 70))
    print(textwrap.fill(s, 40))
    print(textwrap.fill(s, 40, initial_indent="    "))
    print(textwrap.fill(s, 40, subsequent_indent="    "))

    # działa z natywnego terminala, w pycharmie jest symulowany terminal i nie można się dostać do wartości column
    terminal_size = os.get_terminal_size().columns
    print(terminal_size)

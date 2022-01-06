import re
from collections import namedtuple

Token = namedtuple("Token", ["type", "value"])

NAME = r"(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)"
NUM = r"(?P<NUM>\d+)"
PLUS = r"(?P<PLUS>\+)"
TIMES = r"(?P<TIMES>\*)"
EQ = r"(?P<EQ>=)"
WS = r"(?P<WS>\s+)"

text = "foo = 23 + 42 * 10"

master_pat = re.compile("|".join([NAME, NUM, PLUS, TIMES, EQ, WS]))


def generate_token(pat, text):
    scan = pat.scanner(text)
    for m in iter(scan.match, None):
        yield Token(m.lastgroup, m.group())


if __name__ == "__main__":
    scanner = master_pat.scanner("foo = 42")
    match = scanner.match()
    print(match.lastgroup, match.group())
    match = scanner.match()
    print(match.lastgroup, match.group())
    match = scanner.match()
    print(match.lastgroup, match.group())
    match = scanner.match()
    print(match.lastgroup, match.group())
    match = scanner.match()
    print(match.lastgroup, match.group())

    for token in generate_token(master_pat, text):
        print(token)

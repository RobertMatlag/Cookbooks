from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    # 1
    with open("somefile.txt") as f:
        for line, previous_lines in search(f, "python", 3):
            for p_line in previous_lines:
                print(p_line, end="")
            print(line, end="")
            print("-" * 20)

    # 2
    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)

    print(q)

    q.append(4)
    print(q)

    q.append(5)
    print(q)

    # 3
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)

    print(q)
    q.appendleft(4)
    print(q)

    print(q.pop())
    print(q)

    print(q.popleft())
    print(q)

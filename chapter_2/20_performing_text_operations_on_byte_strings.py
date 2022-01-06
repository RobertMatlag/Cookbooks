import re

data = b'Hello World'

if __name__ == '__main__':
    print(data[0:5])

    print(data.startswith(b'Hello'))

    print(data.split())

    print(data.replace(b'Hello', b'Hello Cruel'))

    # 2
    data = bytearray(b'Hello World')

    print(data[0:5])

    print(data.startswith(b'Hello'))

    print(data.split())

    print(data.replace(b'Hello', b'Hello Cruel'))

    # 3
    data = b'FOO:BAR,SPAM'
    print(re.split(b'[:,]', data))


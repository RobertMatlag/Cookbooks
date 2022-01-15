import struct

if __name__ == "__main__":
    data = b"\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004"
    print(len(data))
    print(int.from_bytes(data, "little"))
    print(int.from_bytes(data, "big"))

    x = 94522842520747284487117727783387188
    print(x.to_bytes(16, "big"))
    print(x.to_bytes(16, "little"))

    # 2
    hi, lo = struct.unpack(">QQ", data)
    print(hi)
    print(lo)
    print(hi << 64)
    print((hi << 64) + lo)

    # 3
    x = 0x01020304
    print(x.to_bytes(4, "little"))
    print(x.to_bytes(4, "big"))

    # 4
    x = 523 ** 23
    print(x)
    # print(x.to_bytes(16,  'little'))
    print(x.bit_length())
    nbytes, rem = divmod(x.bit_length(), 8)
    if rem:
        nbytes += 1
    print(nbytes)
    print(x.to_bytes(nbytes,  'little'))

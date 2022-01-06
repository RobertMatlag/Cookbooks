import html
from xml.sax.saxutils import unescape

s = 'Elements are written as "<tag>text</tag>".'

if __name__ == "__main__":
    print(html.escape(s))
    print(html.escape(s, quote=False))

    # 2
    s = "Spicy Jalapeño"
    print(s.encode("ascii", errors="xmlcharrefreplace"))

    # 3
    s = "Spicy &quot;Jalape&#241;o&quot."
    print(html.unescape(s))

    # 4
    t = "The prompt is &gt;&gt;&gt;"
    print(unescape(t))

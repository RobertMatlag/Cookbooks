import re

text = "UPPER PYTHON, lower python, Mixed Python"

if __name__ == "__main__":
    print(re.findall("python", text, flags=re.IGNORECASE))

    # 2 tutaj tylko podmienia na 'snake'
    print(re.sub("python", "snake", text, flags=re.IGNORECASE))

    # 3
    def matchcase(word):
        def replace(m):
            text = m.group()
            if text.isupper():
                return word.upper()
            elif text.islower():
                return word.lower()
            elif text[0].isupper():
                return text.capitalize()
            else:
                return word
        return replace

    print(re.sub('pytohn', matchcase('snake'), text, flags=re.IGNORECASE))


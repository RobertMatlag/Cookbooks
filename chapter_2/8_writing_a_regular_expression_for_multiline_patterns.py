import re

comment = re.compile(r"/\*(.*?)\*/")
text1 = "/* this is a comment */"

text2 = """/* this is a 
            multiline comment */
"""

if __name__ == "__main__":
    print(comment.findall(text1))
    print(comment.findall(text2))

    # żeby szukało w wielu liniach trzeba zmineić pattern, wykorzystanie non-capture group
    comment = re.compile(r"/\*((?:.|\n)*?)\*/")

    print(comment.findall(text1))
    print(comment.findall(text2))

    # wykorystanie flagi, UWAGA: lepiej zrobić konkretny pattern w bardziej skomplikowanych przypadkach,
    # można wykorzystać do prostych przypadków
    comment = re.compile(r"/\*(.*?)\*/", re.DOTALL)
    print(comment.findall(text1))
    print(comment.findall(text2))

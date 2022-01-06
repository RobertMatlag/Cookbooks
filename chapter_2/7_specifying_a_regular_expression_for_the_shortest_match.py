import re

str_pat = re.compile(r"\"(.*)\"")
text1 = 'Computer says "no."'
text2 = 'Computer says "no." Phone says "yes."'

if __name__ == '__main__':
    print(str_pat.findall(text1))
    print(str_pat.findall(text2))

    str_pat = re.compile(r"\"(.*?)\"") # dodanie ? powoduje, że łapie najkrótszy tekst.
    # ('*', '.') są normalnie greedy (zachłane) tzn szukają jak najdłuszego dopasowania

    print(str_pat.findall(text1))
    print(str_pat.findall(text2))

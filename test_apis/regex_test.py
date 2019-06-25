import re

if __name__ == '__main__':
    string = "hola mundo  hh  Media Day cómo"
    #string = re.sub(r"\U0001f499", '', string)
    string = re.sub(r"\u201d", '', string)
    print(string.encode('latin-1', errors='replace'))
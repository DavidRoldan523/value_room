import re
from stop_words import get_stop_words


def clean_string(string):
    stop_words = get_stop_words('spanish')
    string = re.sub(r"[^a-zA-Z]", ' ', string)
    for word in stop_words:
        if re.findall(fr'\b({word})\b', string):
            string = re.sub(fr"\b({word})\b", '', string)
    return string


if __name__ == '__main__':
    string = 'hola mundo # como estan 123  perras\n y al he donde de' \
                 '  carro moto moto Perras hola\n' \
                 '   perras moto ,  moto / ( ) { } ; : {} ' \
                 '? ¡ ¿ ¿ y'.lower()
    response = clean_string(string)
    words_list = response.split()
    words_frequency = [words_list.count(word) for word in words_list]
    list_tuple_words = sorted(set(zip(words_list, words_frequency)), key=lambda x: x[1], reverse=True)
    print(list_tuple_words)


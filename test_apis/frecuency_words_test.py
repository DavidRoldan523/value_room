import re
from stop_words import get_stop_words


def clean_string(string):
    stop_words = get_stop_words('spanish')
    string = re.sub('[^\w]+', ' ', string.lower())
    string = re.sub(r"\b[a-zA-Z]{1}\b", '', string)
    string = re.sub("\d+", '', string)
    for word in stop_words:
        if re.findall(fr'\b({word})\b', string):
            string = re.sub(fr"\b({word})\b", '', string)
    return string


if __name__ == '__main__':
    string = 'El Salvador 1-2 Jamaica \nViví d la emoción Emoción del fútbol con Tigo y h'.lower()
    response = clean_string(string)
    words_list = response.split()
    words_frequency = [words_list.count(word) for word in words_list]
    list_tuple_words = sorted(set(zip(words_list, words_frequency)), key=lambda x: x[1], reverse=True)
    print(list_tuple_words)


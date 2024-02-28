def uppercase_string(input_string):
    """
    Принимает строку и возвращает ее в верхнем регистре.

    :param input_string: входная строка
    :return: строка в верхнем регистре
    """
    return input_string.upper()

def big_words(input_string):
    """
    Эта функция делает заглавными первые буквы каждого слова в заданной строке.
    :param input_string: str - Исходная строка для преобразования.
    :return: str - Преобразованная строка.
    """
    return ' '.join(word.big() for word in input_string.split())

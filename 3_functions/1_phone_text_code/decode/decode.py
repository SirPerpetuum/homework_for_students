def decode_numbers(numbers: str) -> str | None:
    """Декодирует закодированные числа в символы."""
    numbers = numbers.split()
    result = []

    # Словарь для ассоциации чисел и декодированных символов
    mapping = {
        1: {"0": " ", "1": ".", "2": "а", "3": "д", "4": "и", "5": "м", "6": "р", "7": "ф", "8": "ш", "9": "ь"},
        2: {"1": ",", "2": "б", "3": "е", "4": "й", "5": "н", "6": "с", "7": "х", "8": "щ", "9": "э"},
        3: {"1": "?", "2": "в", "3": "ж", "4": "к", "5": "о", "6": "т", "7": "ц", "8": "ъ", "9": "ю"},
        4: {"1": "!", "2": "г", "3": "з", "4": "л", "5": "п", "6": "у", "7": "ч", "8": "ы", "9": "я"},
        5: {str(i): ":" for i in range(10)},  # Для 5-тых у нас только ":"
        6: {str(i): ";" for i in range(10)},  # Для 6-тых у нас только ";"
    }

    for number in numbers:
        if is_correct(number):
            length = len(number)
            first_digit = number[0]
            result.append(mapping[length].get(first_digit, ''))
        else:
            return None

    decoded = ''.join(result)
    return decoded if decoded else None

def is_correct(number: str) -> bool:
    if number[0] == "0":
        return len(number) == 1
    elif number[0] == "1":
        return len(number) <= 6 and all(d == "1" for d in number)
    else:
        return len(number) <= 4 and all(d == number[0] for d in number)

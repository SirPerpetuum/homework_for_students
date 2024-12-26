def format_phone(phone_number: str) -> str:
    """Функция возвращает отформатированный телефон.

    Args:
        phone_number: исходный телефон

    Returns:
        отформатированный телефон
    """
    cleaned_number = phone_number
    for digit in phone_number:
        if digit not in "0123456789":
            cleaned_number = cleaned_number.replace(digit, "")

    if len(cleaned_number) == 11:
        formatted_number = "8 (9" + cleaned_number[2] + cleaned_number[3] + ") " + cleaned_number[4] + cleaned_number[
            5] + cleaned_number[6] + "-" + \
                           cleaned_number[7] + cleaned_number[8] + "-" + cleaned_number[9] + cleaned_number[10]
    elif len(cleaned_number) == 10:
        formatted_number = "8 (9" + cleaned_number[1] + cleaned_number[2] + ") " + cleaned_number[3] + cleaned_number[
            4] + cleaned_number[5] + "-" + \
                           cleaned_number[6] + cleaned_number[7] + "-" + cleaned_number[8] + cleaned_number[9]
    else:
        formatted_number = cleaned_number

    return formatted_number

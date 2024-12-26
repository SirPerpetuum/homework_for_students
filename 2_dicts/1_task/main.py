import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция парсит данные, полученные из внешнего API и приводит их к стандартизированному виду."""
    employee_data = get_employees_info()
    parsed_employees_list = []

    for record in employee_data:
        elements = record.split(" ")
        employee_info = {}

        for index in range(0, len(elements), 2):
            attribute = elements[index]
            value = elements[index + 1]

            if attribute == "id":
                employee_info["id"] = int(value)
            elif attribute == "name":
                employee_info["name"] = value
            elif attribute == "last_name":
                employee_info["last_name"] = value
            elif attribute == "age":
                employee_info["age"] = int(value)
            elif attribute == "position":
                employee_info["position"] = value
            elif attribute == "salary":
                employee_info["salary"] = Decimal(value)

        parsed_employees_list.append(employee_info)

    return parsed_employees_list

def parse_record(line: str) -> dict:
    """
    Разбирает строку журнала в словарь.
    Возбуждает ValueError с понятным сообщением при любых некорректных данных.
    """
    fields = line.split(";")
    if len(fields) != 3:
        raise ValueError(f"Неверное количество полей: ожидалось 3, получено {len(fields)}")

    city, temp_str, date = fields

    if not city.strip():
        raise ValueError("Название города не может быть пустым")
    if not date.strip():
        raise ValueError("Дата не может быть пустой")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Некорректное значение температуры: '{temp_str}' не является числом")
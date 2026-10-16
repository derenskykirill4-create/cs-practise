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

def read_valid(lines: list[str]) -> tuple[list[dict], int]:
    """
    Разбирает список строк. Пустые строки игнорирует.
    Возвращает список корректных записей и счетчик испорченных строк.
    """
    valid_records = []
    errors_count = 0

    for line in lines:
        # Пропускаем пустые строки (или строки, состоящие только из пробелов)
        if not line.strip():
            continue

        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            errors_count += 1

        return valid_records, errors_count

def average_by_city(records: list[dict]) -> dict:
    """
    Вычисляет среднюю температуру по каждому городу.
    """
    totals = {}
    counts = {}

    for r in records:
        city = r["city"]
        totals[city] = totals.get(city, 0.0) + r["temperature"]
        counts[city] = counts.get(city, 0) + 1

    averages = {}
    for city in totals:
        averages[city] = totals[city] / counts[city]

    return averages

def warmest_city(records: list[dict]) -> str:
    """
    Находит город с наибольшей средней температурой.
    При равенстве возвращает первый по алфавиту.
    """
    if not records:
        return ""

    averages = average_by_city(records)

    # Сортируvdbbfdkmbfkем: сначала по температуре (по убыванию),
    # затем по названию города (по алфавиту / возрастанию)
    sorted_cities = sorted(
        averages.items(),
        key=lambda item: (-item[1], item[0])
    )

    return sorted_cities[0][0]


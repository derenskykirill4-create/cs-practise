def parse_record(line: str) -> dict:
    """
    Разбирает строку «город;температура;дата» в словарь.
    Возбуждает ValueError с понятным сообщением, если данные некорректны.
    """
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Неверное количество полей: ожидалось 3, получено {len(parts)}")

    city, temp_str, date = parts

    if not city.strip():
        raise ValueError("Название города не может быть пустым")
    if not date.strip():
        raise ValueError("Дата не может быть пустой")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Некорректный формат температуры: '{temp_str}' не является числом")

    return {
        "city": city.strip(),
        "temp": temp,
        "date": date.strip()
    }


def read_valid(lines: list[str]) -> tuple[list[dict], int]:
    """
    Разбирает строки журнала. Пустые строки пропускаются молча.
    Возвращает кортеж: (список корректных записей, количество ошибочных строк).
    """
    valid_records = []
    errors_count = 0

    for line in lines:
        if not line.strip():  # Пустые строки пропускаются молча
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
    Возвращает словарь {город: средняя_температура}.
    """
    totals = {}
    counts = {}

    for r in records:
        city = r["city"]
        totals[city] = totals.get(city, 0.0) + r["temp"]
        counts[city] = counts.get(city, 0) + 1

    averages = {}
    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)

    return averages


def warmest_city(records: list[dict]) -> str:
    """
    Находит город с наибольшей средней температурой.
    При равенстве возвращает первый по алфавиту.
    """
    if not records:
        return ""

    averages = average_by_city(records)

    # Сортируем: сначала по температуре (по убыванию), затем по названию (по алфавиту)
    # Чтобы по алфавиту шел «первый», мы используем знак минус перед температурой при сортировке по возрастанию
    best_city = min(averages.keys(), key=lambda city: (-averages[city], city))
    return best_city
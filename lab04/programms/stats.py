def parse_record(line: str) -> dict:
    """Разбирает одну строку журнала. Возбуждает ValueError, если данные некорректны."""
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно 3 поля, разделенных ';'")

    city, temp_str, date = parts

    if not city.strip():
        raise ValueError("Имя города не может быть пустым")
    if not date.strip():
        raise ValueError("Дата не может быть пустой")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Некорректное значение температуры: '{temp_str}'")

    return {"city": city, "temp": temp, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    """Разбирает список строк. Пропускает пустые и битые строки, считая ошибки."""
    valid_records = []
    invalid_count = 0

    for line in lines:
        if not line.strip():
            continue  # Пустые строки пропускаются молча
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            invalid_count += 1

    # Сохраняем счетчик испорченных строк прямо в атрибут функции (или списка),
    # чтобы main.py мог получить к нему доступ, не ломая сигнатуру.
    read_valid.invalid_count = invalid_count
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    """Вычисляет среднюю температуру по городам, округляя до 1 знака."""
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
    """Находит самый теплый город. При равенстве температур — первый по алфавиту."""
    if not records:
        return ""

    averages = average_by_city(records)

    # Сортируем: сначала по температуре (по убыванию), затем по имени города (по алфавиту)
    # Чтобы алфавитный порядок шел "от А до Я", используем минус перед температурой при сортировке,
    # либо стандартный max с хитрым ключом:
    best_city = max(averages.keys(), key=lambda c: (averages[c], [-ord(char) for char in c]))
    return best_city

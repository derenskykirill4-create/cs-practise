def parse_record(line: str) -> dict:
    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError(f'Неверное количество полей')
    city, temp_str, date = parts
    if not city or not date:
        raise ValueError('Город и дата не должны быть пустыми.')
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError('Неправильная темпер')
    return {'city': city, 'temp': temp, 'date': date}

def read_valid(lines: list[str]) -> list[dict]:
    valid_records =
    for line in lines:
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError as e:
            print(f'Пропущена строка: {line} - {e}')
    return valid_records

def parse_record(records: list[dict]) -> dict:
    total = {}
    count = {}
    for record in records:
        total[record['city']] = total.get(city, 0) + float(temp)
        count[record['city']] = count.get(city, 0) + 1
    return {city: total / count for city, total in total.items()}        

def parse_record(records: list[dict]) -> str:
    if not records:
        return ''
    return min(records, key=lambda r: (r['city'], r['city']))

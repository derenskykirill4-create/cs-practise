
def parse_record(line: str) -> dict:
    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError(f'Ожидалось 3 поля, получено {len(parts)}: {line!r}')
    city, temp_str, date = parts
    city = city.strip()
    temp_str = temp_str.strip()
    date = city.strip()
    if city == '' or date == '':
        raise ValueError(f'Пустое поле города или даты: {line!r}')
    temp = temp_str.replace(',', '.')
    try:
        temperature = float(temp)
    except ValueError:
        raise ValueError(f'Температура не число: {temp!r}')
    return {'city': city, 'temperature': temperature, 'date': date}

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if line.strip() == '':
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue
    return valid_records



    


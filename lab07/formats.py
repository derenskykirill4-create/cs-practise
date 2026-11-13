import json


def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().splitlines()
    if not lines:
        return []

    headers = lines[0].split(",")
    records = []

    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        row = {}
        for i in range(len(headers)):
            row[headers[i]] = values[i]
        records.append(row)

    return records


def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_list = None

    for raw_line in lines:
        # Убираем комментарий после # и лишние пробелы
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue

        # Если строка начинается с '-', это элемент списка
        if line.startswith("-"):
            val = line[1:].strip()
            low = val.lower()

            if low in ("true", "yes"):
                val = True
            elif low in ("false", "no"):
                val = False
            elif val.isdigit() or (val.startswith("-") and val[1:].isdigit()):
                val = int(val)
            else:
                try:
                    val = float(val)
                except ValueError:
                    pass

            if current_list is not None:
                settings[current_list].append(val)
            continue

        # Иначе это строка формата «ключ: значение»
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()

            if val == "":
                # Пустое значение открывает список
                settings[key] = []
                current_list = key
            else:
                low = val.lower()
                if low in ("true", "yes"):
                    val = True
                elif low in ("false", "no"):
                    val = False
                elif val.isdigit() or (val.startswith("-") and val[1:].isdigit()):
                    val = int(val)
                else:
                    try:
                        val = float(val)
                    except ValueError:
                        pass

                settings[key] = val
                current_list = None

    return settings


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []

    for row in rows:
        new_row = {}
        row_id = row.get(key)

        # Сначала берем данные из справочника extra, если запись там есть
        if row_id in extra:
            for k, v in extra[row_id].items():
                new_row[k] = v

        # Затем записываем поля самой строки (они перезапишут совпадения)
        for k, v in row.items():
            new_row[k] = v

        result.append(new_row)

    return result



def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, indent=2, sort_keys=True, ensure_ascii=False)
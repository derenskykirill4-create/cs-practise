# Разрешенные уровни логирования
VALID_LEVELS = {"INFO", "ERROR", "BROKEN", "WARNING"}


def parse_event(line: str) -> dict:
    """
    Разбирает строку журнала «время уровень сообщение» в словарь.
    Если строка негодная, выбрасывает ValueError.
    """
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")

    # Разделяем строку максимум на 3 части по пробелам
    parts = line.split(maxsplit=2)

    # Если частей меньше 3, значит отсутствует сообщение или уровень
    if len(parts) < 3:
        raise ValueError("Недостаточно элементов в строке лога")

    time, level, message = parts

    # Проверяем корректность уровня
    if level not in VALID_LEVELS:
        raise ValueError(f"Неизвестный уровень логирования: {level}")

    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    """
    Считает количество строк каждого уровня.
    Испорченные строки учитываются под ключом BROKEN. Пустые пропускаются.
    """
    counts = {"INFO": 0, "ERROR": 0, "BROKEN": 0, "WARNING": 0}

    for line in lines:
        cleaned = line.strip()
        if not cleaned:  # Пропускаем пустые строки
            continue
        try:
            event = parse_event(cleaned)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1

    return counts


def top_errors(lines, n: int) -> list[list]:
    """
    Возвращает n самых частых сообщений уровня ERROR: пары [сообщение, сколько раз].
    При равенстве частоты — сортировка по алфавиту сообщения.
    """
    error_counts = {}

    for line in lines:
        cleaned = line.strip()
        if not cleaned:
            continue
        try:
            event = parse_event(cleaned)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue  # Пропускаем битые строки

    # Сортировка: сначала по убыванию частоты (-x[1]), затем по алфавиту (x[0])
    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))

    # Преобразуем кортежи в списки и берем первые n элементов
    return [list(item) for item in sorted_errors[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    """
    Формирует финальный текст отчёта.
    Уровни выводятся строго по алфавиту. В конце текста — перевод строки.
    """
    lines = ["Отчёт по журналу"]

    # Сортируем ключи словаря counts по алфавиту (BROKEN, DEBUG, ERROR, INFO, WARNING)
    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")

    lines.append("Частые ошибки:")
    for msg, count in errors:
        lines.append(f"- {msg} — {count}")

    # Объединяем строки и добавляем перевод строки в самом конце файла
    return "\n".join(lines) + "\n"
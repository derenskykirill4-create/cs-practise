import collections

VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    """Разбирает строку журнала на компоненты.
    Если строка некорректна, генерирует ValueError.
    """
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")

    # Разделяем максимум на 3 части (время, уровень, сообщение)
    parts = line.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Строка содержит недостаточно элементов")

    time, level, message = parts

    if level not in VALID_LEVELS:
        raise ValueError(f"Неизвестный уровень логирования: {level}")

    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    """Считает количество строк каждого уровня.
    Испорченные строки учитывает под ключом BROKEN.
    """
    # Инициализируем словарь со всеми возможными уровнями и BROKEN
    counts = {level: 0 for level in VALID_LEVELS}
    counts["BROKEN"] = 0

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
    """Возвращает n самых частых сообщений уровня ERROR.
    При равенстве частоты сортирует по алфавиту.
    """
    error_counts = collections.Counter()

    for line in lines:
        cleaned = line.strip()
        if not cleaned:
            continue
        try:
            event = parse_event(cleaned)
            if event["level"] == "ERROR":
                error_counts[event["message"]] += 1
        except ValueError:
            continue  # Игнорируем битые строки для подсчета ошибок

    # Сортировка: сначала по убыванию частоты (-x[1]), затем по алфавиту (x[0])
    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))

    # Преобразуем кортежи в списки списков, как требуется в условии
    return [list(item) for item in sorted_errors[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    """Формирует финальный текстовый отчёт."""
    report_lines = ["Отчёт по журналу", ""]

    # Уровни сортируем по алфавиту (BROKEN, DEBUG, ERROR, INFO, WARNING)
    for level in sorted(counts.keys()):
        report_lines.append(f"{level}: {counts[level]}")

    report_lines.extend(["", "Частые ошибки:"])
    for msg, count in errors:
        report_lines.append(f"- {msg} — {count}")

    # В конце текста обязательно должен быть перевод строки
    return "\n".join(report_lines) + "\n"
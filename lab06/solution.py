from pathlib import Path # импортируем
paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

def count_by_extension(paths: list[str]) -> dict[str, int]:
    extensions = {} # используем словарь для нахождения расширения файлов
    for p in paths:
        p = Path(p) # разбиваем каждый путь на части
        ext = p.suffix.lower().lstrip('.')
        if p.name.startswith('.'): # с помощью метода .name ищем имена, где есть расширение
            ext = ''

        extensions[ext] = extensions.get(ext, 0) + 1
    return extensions

def deepest_path(paths: list[str]) -> str:
    if not paths: # Проверяем, есть ли / в списке?
        return ''
    else:
        deep = paths[0]
        max1 = len(Path(deep).parts) # Берём за максимальную длину первый расчленённый путь
        for p in paths:
            p_str = Path(p) # Разбиваем на части
            p_obj = p_str.parts
            curr = len(p_obj) # Ищем длину нынешнего списка
            if curr > max1: # сравниваем длины
                max1 = curr
                deep = p # запоминаем глубину
    return deep


def human_size(n_bytes: int) -> str:
    if n_bytes == 0:
        return "0 Б"

    suffixes = ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ"]
    n_bytes = float(n_bytes)
    i = 0

    # Переводим в нужную единицу измерения
    while n_bytes >= 1024 and idx < len(suffixes) - 1:
        n_bytes = n_bytes / 1024.0
        i += 1

    # Если единица измерения - Байты (Б), форматируем как целое число
    if i == 0:
        return f"{int(n_bytes)} Б"

    # Для всех остальных (КБ, МБ, ГБ...) - всегда 1 знак после запятой (например, 5.0 МБ)
    return f"{n_bytes:.1f} {suffixes[i]}"


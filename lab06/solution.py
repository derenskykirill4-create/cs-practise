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
    suffixes = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ'] # выписываем все обозначения
    i = 0
    while n_bytes >= 1024 and i < len(suffixes) - 1:  # Проверяем, чтобы число было больше 1024 и
        # индекс был меньше длины списка с обозначениями - 1, т.к. последовательность начинается с 0.
        n_bytes = n_bytes / 1024
        i = i + 1
        if n_bytes.is_integer(): # Если найдётся хотя бы одно целое число, то хаписываем его без '.0'
            print('%d %s' % (n_bytes, suffixes[i]))
    return '%.1f %s' % (n_bytes, suffixes[i])


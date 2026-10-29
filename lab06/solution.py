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


def human_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0 Б"

    labels = ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ"]
    size = float(size_bytes)

    # Делим на 1024, пока размер больше или равен 1024
    # Но для байт (labels[0]) деление не должно происходить, если размер < 1024
    idx = 0
    while size >= 1024 and idx < len(labels) - 1:
        size /= 1024.0
        idx += 1

    # Округляем до 1 знака после запятой
    size = round(size, 1)

    # Убираем .0, если число целое
    if size.is_integer():
        return f"{int(size)} {labels[idx]}"

    return f"{size} {labels[idx]}"
'''def human_size(n_bytes: int) -> str:
    suffixes = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ'] # выписываем все обозначения
    i = 0
    while n_bytes >= 1024 and i < len(suffixes) - 1:  # Проверяем, чтобы число было больше 1024 и
        # индекс был меньше длины списка с обозначениями - 1, т.к. последовательность начинается с 0.
        n_bytes = n_bytes / 1024
        i = i + 1
        if n_bytes.is_integer(): # Если найдётся хотя бы одно целое число, то хаписываем его без '.0'
            print('%d %s' % (n_bytes, suffixes[i]))
            
    return '%.1f %s' % (n_bytes, suffixes[i])'''


from pathlib import Path # импортируем
paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

def count_by_extension(paths: list[str]) -> dict[str, int]:
    extensions = {} # используем словарь для нахождения расширения файлов
    for p in paths:
        p = Path(p) # разбиваем каждый путь на части
        ext = p.suffix
        if p.name.startswith('.'): # с помощью метода .name ищем имена, где есть расширение
            ext = ''

        extensions[ext] = extensions.get(ext, 0) + 1
    return extensions

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ''
    else:
        deep = paths[0]
        max1 = len(Path(deep).parts)
        for p in paths:
            p_str = Path(p)
            p_obj = p_str.parts
            curr = len(p_obj)
            if curr > max1:
                max1 = curr
                deep = p
    return deep

def human_size(n_bytes: int) -> str:
    suffixes = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    i = 0
    while n_bytes >= 1024 and i < len(suffixes) - 1:
        n_bytes = n_bytes / 1024
        i = i + 1

    return '%3.1f %s' % (n_bytes, suffixes[i])


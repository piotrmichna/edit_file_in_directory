from pathlib import Path

replace_char = [
    {'char': ' ', 'replace': '_'},
    {'char': '.', 'replace': '_'},
    {'char': '@', 'replace': 'a'},
    {'char': '$', 'replace': 's'},
    {'char': '&', 'replace': 'and'}
]
file_types = ['*.txt', '*.tx']


def file_name_split(name) -> list:
    file_list = name.split('.')
    if len(file_list) == 1:
        file_list.append(False)
    elif len(file_list) > 2:
        return ['.'.join(file_list[:-1]), file_list[-1]]
    return file_list


def file_name_clean(filename):
    filename = str(filename)
    while filename[0] == ' ':
        filename = filename[1:]
    while filename[-1] == ' ':
        filename = filename[:-1]

    for char in replace_char:
        if char['char'] in filename:
            filename_list = filename.split(char['char'])
            filename = char['replace'].join(filename_list)
    return filename


def file_get_new_path(path: Path) -> Path:
    path = str(path)
    if '/' in path:
        file = path.split('/')
        path_char = '/'
    elif '\\' in path:
        file = path.split('\\')
        path_char = '\\'

    filename = file[-1]
    filename = file_name_split(filename)
    filename[0] = file_name_clean(filename[0])
    if filename[1]:
        file[-1] = '.'.join(filename)
    else:
        file[-1] = filename[0]

    path = path_char.join(file)
    return Path(path)


if __name__ == '__main__':
    print(file_name_split('Dokument tekstowy.txt'))

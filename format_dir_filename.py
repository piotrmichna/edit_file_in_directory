from pathlib import Path

replace_char = [
    {'char': ' ', 'replace': '_'},
    {'char': '.', 'replace': '_'},
    {'char': '@', 'replace': 'a'},
    {'char': '$', 'replace': 's'},
    {'char': '&', 'replace': 'and'}
]


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


def file_get_new_path(path) -> Path:
    return Path(path)


if __name__ == '__main__':
    print(file_name_split('Dokument tekstowy.txt'))

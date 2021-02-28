import os
from pathlib import Path

replace_char = [
    {'char': ' ', 'replace': '_'},
    {'char': '.', 'replace': '_'},
    {'char': '@', 'replace': 'a'},
    {'char': '$', 'replace': 's'},
    {'char': '#', 'replace': 'x'},
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


def get_file_path_list():
    file_list = []
    for file_type in file_types:
        file_list.extend(list(Path.cwd().glob(file_type)))
    return file_list


def get_not_correct_file_list():
    file_list = get_file_path_list()
    not_correct_list = []
    for file_path in file_list:
        new_file_path = file_get_new_path(file_path)
        if new_file_path != file_path:
            not_correct_list.append({'old': file_path, 'new': new_file_path})

    flag = 1
    while flag:
        flag = 0
        for x in range(0, len(not_correct_list)):
            filenamex = file_name_split(not_correct_list[x]['new'].name)

            for y in range(0, len(file_list)):
                filenamey = file_name_split(file_list[y].name)
                if filenamex[0] == filenamey[0]:
                    flag += 1
                    numb = ''
                    nx = filenamex[0][-1]
                    while nx.isdigit():
                        numb = numb + nx
                        filenamex[0] = filenamex[0][0:-1]
                        nx = filenamex[0][-1]

                    if numb != '':
                        if len(numb) > 1:
                            numb = str(numb)[::-1]

                        numb = int(numb)
                        numb += 1
                    else:
                        numb = 0

                    filenamex[0] = filenamex[0] + str(numb)
                    if filenamex[1]:
                        filename = '.'.join(filenamex)
                    else:
                        filename = filenamex[0]

                    file_path = str(not_correct_list[x]['new'])
                    file_path = file_path.split('/')
                    file_path[-1] = filename
                    file_path = '/'.join(file_path)
                    not_correct_list[x]['new'] = Path(file_path)
                    break
    return not_correct_list


def get_rename_file():
    print('---SPRAWDZENIE POPRAWNOŚCI NAZW---')
    path_list = get_not_correct_file_list()
    n = 1
    for path in path_list:
        print(f"{n}. {path['old']} -> {path['new']}")
        n += 1
        os.rename(path['old'], path['new'])

    print('-----------------------------------')


if __name__ == '__main__':
    get_rename_file()

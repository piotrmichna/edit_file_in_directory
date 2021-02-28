import os
from pathlib import Path
from time import sleep

from format_dir_filename import file_types, file_name_split, get_rename_file

EDITED_END_FILE_PATTERN = None
EDITED_FILE_EXTENSION = 'txt'
SLEEP_SEC = 5


def get_file_path_list():
    file_list = []
    for file_type in file_types:
        file_list.extend(list(Path.cwd().glob(file_type)))
    file_list_to_edit = []
    n = 1
    for file in file_list:
        file_name_li = file_name_split(file.name)
        if EDITED_END_FILE_PATTERN or EDITED_FILE_EXTENSION:
            file_name = file_name_li[0]
            if len(file_name_li) > 1:
                file_ext = file_name_li[1]
            else:
                file_ext = None
            if EDITED_FILE_EXTENSION:
                file_ext = EDITED_FILE_EXTENSION

            if EDITED_END_FILE_PATTERN:
                file_pattern = file_name[-2:]
                if file_pattern != EDITED_END_FILE_PATTERN:
                    file_name = f'{file_name}{EDITED_END_FILE_PATTERN}'
            if file_ext:
                file_name = f'{file_name}.{file_ext}'

            new_file = str(file).split('/')
            new_file[-1] = file_name
            new_file = Path('/'.join(new_file))
            file_list_to_edit.append({'file': file, 'edited': new_file})
            print(f'{n}. file to edit={file.name} edited={new_file.name}')
            n += 1

        else:
            file_list_to_edit.append({'file': file, 'edited': None})
            print(f'{n}. file to edit={file.name}')
            n += 1

    return file_list_to_edit


def get_file_edit():
    get_rename_file()
    file_list = get_file_path_list()
    print('---EDIT FILE INSTRUCTIONS---')
    n = 1
    for file in file_list:
        print(f'{n}. Edycja pliku [{file["file"].name}]')
        # DZIALANIA NA PLIKU
        s = 0
        while s < SLEEP_SEC:
            sleep(1)
            s += 1
            print('-', end='')
        print('')
        if file['edited']:
            os.rename(file['file'], file['edited'])
            print(f'{n}. Zmiana nazwy: {file["file"].name} -> {file["edited"].name}')
        n += 1
    print('----------------------------')


if __name__ == '__main__':
    get_file_edit()

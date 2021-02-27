def file_name_split(name) -> list:
    file_list = name.split('.')
    if len(file_list) == 1:
        file_list.append(False)
    elif len(file_list) > 2:
        return ['.'.join(file_list[:-1]), file_list[-1]]
    return file_list

def file_name_clean(filename):
    return filename

if __name__ == '__main__':
    print(file_name_split('Dokument tekstowy.txt'))

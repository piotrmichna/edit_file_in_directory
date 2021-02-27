import pytest

from format_dir_filename import file_name_split


@pytest.mark.parametrize('filename, expected', (
        ('Dokument textowy.txt', ['Dokument textowy', 'txt']),
        ('Dokument.textowy.txt', ['Dokument.textowy', 'txt']),
        ('Dokument text.txt', ['Dokument text', 'txt']),
        ('Dokument.txt', ['Dokument', 'txt']),
        ('Dokument', ['Dokument', False])
))
def test_file_name_split(filename, expected):
    assert expected == file_name_split(filename)

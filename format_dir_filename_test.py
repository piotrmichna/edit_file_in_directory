import pytest

from format_dir_filename import (file_name_split, file_name_clean)


@pytest.mark.parametrize('filename, expected', (
        ('Dokument textowy.txt', ['Dokument textowy', 'txt']),
        ('Dokument.textowy.txt', ['Dokument.textowy', 'txt']),
        ('Dokument.textowy', ['Dokument', 'textowy']),
        ('Dokument text.txt', ['Dokument text', 'txt']),
        ('Dokument.txt', ['Dokument', 'txt']),
        ('Dokument', ['Dokument', False])
))
def test_file_name_split(filename, expected):
    assert expected == file_name_split(filename)


@pytest.mark.parametrize('filename, expected', (
        ('Dokument textowy', 'Dokument_textowy'),
        ('Dokument.textowy', 'Dokument_textowy'),
        ('  Dokument.textowy ', 'Dokument_textowy'),
        ('Dokument & textowy ', 'Dokument_and_textowy'),
        ('Dok@ment textowy ', 'Dokament_textowy'),
        ('Dok$ment textowy ', 'Doksment_textowy'),
        ('Dokument', 'Dokument')
))
def test_file_name_clean(filename, expected):
    assert expected == file_name_clean(filename)

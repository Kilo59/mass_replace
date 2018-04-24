# -*- coding: utf-8 -*-
"""
tests_basic.py
~~~~~~~~~~~~~~
Basic unit tests for `mass_replace` python module written using pytest.
"""
from sys import version_info
from os import path
# from os import chdir
import pytest
try:
    import mass_replace as mr
except ImportError:
    from context import mass_replace as mr


PYTHON_VER = version_info[0]


def read_file_lines(filename):
    """Reads the lines of a file as a list"""
    with open(filename, mode='r') as f_in:
        return f_in.readlines()


def test_mass_replace_import():
    assert isinstance(mr.__doc__, str)
    print(type(mr))


def test_correct_working_dir():
    pass


@pytest.mark.skipif(PYTHON_VER <= 2,
                    reason="List comprehension error with Python 2")
def test_load_config():
    load_config_return_type = type(mr.load_config('mass_replace/config.yaml'))
    print(load_config_return_type, dict)
    assert load_config_return_type is dict


@pytest.mark.skipif(PYTHON_VER <= 2,
                    reason="List comprehension error with Python 2")
def test_get_items():
    assert type(mr.get_items()) is list


@pytest.mark.skipif(PYTHON_VER <= 2,
                    reason="List comprehension error with Python 2")
def test_get_dirs():
    assert type(mr.get_dirs()) is list


@pytest.mark.skipif(PYTHON_VER <= 2,
                    reason="List comprehension error with Python 2")
def test_get_files():
    """Test that `get_files()` returns a list and that every item within the
    list is a file."""
    files = mr.get_files()
    assert type(files) is list
    for f in files:
        assert path.isfile(f)


def test_simple_file_find_and_replace():
    """Replace text in the lorem.txt file and undo it."""
    filename = 'mass_replace/lorem.txt'
    mr.file_find_replace(filename, 'Lorem', 'REPLACED')
    first_str = read_file_lines(filename)[0].split(' ')[0]
    assert first_str == 'REPLACED'
    mr.file_find_replace(filename, 'REPLACED', 'Lorem')
    first_str = read_file_lines(filename)[0].split(' ')[0]
    assert first_str == 'Lorem'


def test_basic_mass_replace():
    config_dict = {'filetypes': ['txt', 'csv'],
                   'replacement_pairs': {'a': 'z'}}
    mr.mass_replace('tests\\docs', config=config_dict)
    txt_1st_str = read_file_lines('tests\\docs\\abc.txt')[0][0]
    csv_1st_str = read_file_lines('tests\\docs\\abc.csv')[0][0]
    assert txt_1st_str == config_dict['replacement_pairs']['a']
    assert csv_1st_str == config_dict['replacement_pairs']['a']
    # reset files
    config_dict['replacement_pairs'] = {'z': 'a'}
    mr.mass_replace('tests\\docs', config=config_dict)
    txt_1st_str = read_file_lines('tests\\docs\\abc.txt')[0][0]
    csv_1st_str = read_file_lines('tests\\docs\\abc.csv')[0][0]
    assert txt_1st_str == config_dict['replacement_pairs']['z']
    assert csv_1st_str == config_dict['replacement_pairs']['z']


if __name__ == '__main__':
    print('Python: {}.{}'.format(version_info[0], version_info[1]))
    print(__doc__)
    pytest.main(args=['-v'])
    # print(test_load_config())
    # print(test_mass_replace_import())

import pytest
from wiki import page_by_name, load_page_by_name


def test_basic_page_load():
    data, status_code = load_page_by_name('Вкус ночи')
    assert 'Вкус ночи' in data
    assert len(data) > 50000
    assert status_code == 200

import pytest
from pathlib import Path
from source.standard_pad_module import cleaner



pad = Path(r"C:\Users\Dhr. Ten Hoonte\PycharmProjects\Projekt_lijstbewerken\test\tmp")


def test_cleaner():
    expected = 0
    fail = cleaner(pad)
    assert fail == expected


print(pad.is_dir())

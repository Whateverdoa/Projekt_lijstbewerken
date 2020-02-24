from source.counter_of_lists import myfile, totaal


def test_file():

    assert myfile == r'\bestanden\201922020_lijst.csv'


def test_totaal():
    assert totaal == 229280


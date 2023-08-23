from coffee.latte import latte


def test_latte():
    assert latte.make() == "latte"

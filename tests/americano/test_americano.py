from coffee.americano import americano


def test_americano():
    assert americano.make() == "americano"

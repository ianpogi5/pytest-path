from coffee.main import main


def test_main_latte():
    captured = main("latte")
    assert captured == "I created latte"


def test_main_americano():
    captured = main("americano")
    assert captured == "I created americano"


def test_main_invalid():
    captured = main("invalid")
    assert captured == "I created americano"

from .americano import americano
from .latte import latte


def main(coffee_type):
    coffee = ""
    if coffee_type == 'latte':
        coffee = latte.make()
    else:
        coffee = americano.make()
    return f"I created {coffee}"

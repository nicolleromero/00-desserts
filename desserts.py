"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __init__(self, name, flavor, price):

        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0

        self.cache[self.name] = self

    def add_stock(self, amount):
        """Add the amount to self.qty"""

        self.qty = self.qty + amount

    def sell(self, amount):
        """Sell the given amount of cupcakes and update self.qty"""

        if self.qty == 0:
            print("Sorry, these cupcakes are sold out")
        elif self.qty - amount < 0:
            self.qty = 0
        else:
            self.qty = self.qty - amount

    @staticmethod
    def scale_recipe(ingredients, amount):
        """Scale the list of ingredients by the given amount of cupcakes."""

        scaled_ingredients = []
        for ingredient in ingredients:
            scaled_ingredients.append((ingredient[0], ingredient[1] * amount))

        return scaled_ingredients

    @classmethod
    def get(cls, name):
        """Return a cupcake from cls.cache"""

        if name in cls.cache:
            return cls.cache[name]
        else:
            print("Sorry, that cupcake doesn't exist")

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')

# test_cupcake = Cupcake()
# test_cupcake

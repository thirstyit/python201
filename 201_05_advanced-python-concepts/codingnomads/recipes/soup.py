# from ..ingredients import Ingredient
# from ..codingnomads.ingredients import Ingredient

class Soup():
    def __init__(self, *args):
        self.args = args
    def __str__(self):
        return str(self.args)

    
# print(Ingredient())
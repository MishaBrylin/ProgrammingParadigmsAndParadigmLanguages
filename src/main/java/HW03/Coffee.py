class Coffee:
    def __init__(self):
        self.cost_value = 100

    def cost(self):
        return self.cost_value


class Sugar:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 10


class Milk:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 30


coffee = Coffee()
coffee = Sugar(coffee)


print(coffee.cost())
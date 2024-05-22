class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} открыт!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, couisine_type):
        super().__init__(restaurant_name, couisine_type)
        self.flavors = []

    def flavors(self):
        for icecream in self.flavors:
            print (f"Сорт мороженного - {icecream}")
icecream1 = IceCreamStand("ICECREAM", "мороженое")

icecream1.flavors

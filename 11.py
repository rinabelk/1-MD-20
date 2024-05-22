class Restaurant:

    def __init__(restor, restaurant_name, cuisine_type):
        restor.restaurant_name = restaurant_name
        restor.cuisine_type = cuisine_type

    def describe_restaurant(restor):
        print(f"Название ресторана: {restor.restaurant_name}")
        print(f"Тип кухни: {restor.cuisine_type}")

    def open_restaurant(restor):
        print(f"{restor.restaurant_name} открыт!")



newRestaurant = Restaurant("Марчелиз", "итальянская")

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

resta1 = Restaurant("Токио Сити", "кухни всех видов")
resta2 = Restaurant("ДедХо", "въетнамская")
resta3 = Restaurant("Korean", "корейская")


resta1.describe_restaurant()
resta2.describe_restaurant()
resta3.describe_restaurant()

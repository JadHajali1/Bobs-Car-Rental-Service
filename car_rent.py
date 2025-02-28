class Vehicle:

    brand = ""
    model = ""
    year = 0
    rental_price_per_day = 0

    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_day = rental_price_per_day

    def display_info(self):
        print(f"")

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days


   


class Car(Vehicle):
    seating_capacity = 0




class Bike(Vehicle):
    engine_capacity = ""


    
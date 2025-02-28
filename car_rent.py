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
        print(f"{self.brand} {self.model}, Year:{self.year}, Rental Price: ${self.rental_price_per_day}/day")

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days


   


class Car(Vehicle):
    def __init__(self, brand, model, year, seating_capacity,rental_price_per_day):
        self.seating_capacity = seating_capacity
        super().__init__(brand, model, year, rental_price_per_day)




class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_capacity,rental_price_per_day):
        self.engine_capacity = engine_capacity
        super().__init__(brand, model, year, rental_price_per_day)


    
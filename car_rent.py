class vehicle:

    brand = ""
    model = ""
    year = 0
    rental_price_per_day = 0

    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_day = rental_price_per_day

   


class type:
    seating_capacity = 0
    engine_capacity = ""

    def __init__(self, seating_capacity, engine_capacity):
        self.seating_capacity = seating_capacity
        self.engine_capacity = engine_capacity
        



    
class CustomerRents:

    brand = ""
    model = ""
    year = 0
    rental_price_per_day = 0

    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_day = rental_price_per_day
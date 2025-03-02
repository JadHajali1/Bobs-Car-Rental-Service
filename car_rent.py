class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day

    def get_rental_price_per_day(self):
        return self.__rental_price_per_day

    def set_rental_price_per_day(self,price):
        if price > 0:
            self.__rental_price_per_day = price
        else:
            print("price can't be nigative")


    def display_info(self):
        print(f"{self.brand} {self.model}, Year:{self.year}, Rental Price: ${self.get_rental_price_per_day()}/day")

    def calculate_rental_cost(self, days):
        return self.get_rental_price_per_day() * days



class Car(Vehicle):
    def __init__(self, brand, model, year, seating_capacity, rental_price_per_day):
        self.seating_capacity = seating_capacity
        super().__init__(brand, model, year, rental_price_per_day)

    def display_info(self):
        print(f"{self.brand} {self.model}, Year:{self.year},Seats: {self.seating_capacity},Rental Price: ${self.get_rental_price_per_day()}/day")


class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_capacity, rental_price_per_day):
        self.engine_capacity = engine_capacity
        super().__init__(brand, model, year, rental_price_per_day)
    
    def display_info(self):
        print(f"{self.brand} {self.model}, Year:{self.year},Engine: {self.engine_capacity}cc, Rental Price: ${self.get_rental_price_per_day()}/day")


def show_vehicle_info(vehicle):
    vehicle.display_info()




def car_types():
    print("****************************************")
    print("chose your type of Car:")
    print("1:Toyota Corolla 2023 --> $44/day ")
    print("2:Toyota Camry 2022 --> $50/day")
    print("3: Honda CRV 2024 --> $40/day")
    print("4:Suzuki Solio 2022 --> $48/day")
    print("5:Ford Tierra 2025 --> $45/day")
    print("****************************************")

def bike_types():
    print("****************************************")
    print("chose your type of Bike:")
    print("1:Bikes Seaside 300 2025 --> $35/day")
    print("2:Aima Big sur 800 2024 --> $25/day")
    print("3:Muon Aspire 500 2025 --> $30/day")
    print("4:Jamis Coda S1 1300 2020 --> $40/day")
    print("****************************************")


car1 = Car("Toyota", "Corolla", 2023, 5, 44)
car2 = Car("Toyota", "Camry", 2022, 5, 50)
car3 = Car("THonda ", "Camry", 2024, 5, 40)
car4 = Car("Suzuki", "Aspire", 2022, 5, 48)
car5 = Car("Ford", "Tierra", 2025, 5, 45)
cars = [car1, car2, car3, car4, car5]

bike1 = Bike("Bikes", "Seaside", 2025, 300, 35)
bike2 = Bike("Aima", "Big sur", 2024, 800, 25)
bike3 = Bike("Muon", "Seaside", 2025, 500, 30)
bike4 = Bike("Jamis", "Coda S1", 2020, 1300, 40)


print("Welcome to Bob's Car Rental Service!!")
print("whold you like to rent a Cars or Bikes?")
agremment = input("Yes to countinue No to stop!!").lower()

while agremment == "yes":

    print("We offer Cars and Bikes")
    choice = input("choose Car to see Car list or Bike to see Bike list:").lower()

    if choice =="car":
        car_types()
        print()
        car_num = input("please Enter the number of the car that you want to rent: ")

        if car_num == 1:
            show_vehicle_info(car1)
        elif car_num == 2:
            show_vehicle_info(car2)
        elif car_num == 3:
            show_vehicle_info(car3)
        elif car_num == 4:
            show_vehicle_info(car4)
        elif car_num == 5:
            show_vehicle_info(car5)
        else:
            print("please choose any number from the list!!")
        
        
        print("please enter how many days you want to rent this car: ")
        rental_days = int(input("days: "))

        print(f"Rental cost for {car.brand} Corolla for {rental_days} days: {car}")

        print("Do you Suggest another price for this car?")
        suggestion = input("Enter yes to change the price or no to keep it the same: ").lower()

        if suggestion == "yes":
            new_price = int(input("Enter your suggestion price: "))
            if new_price > 0:
                print("Your suggestion can't be negative")
            else:
                print(f"Updated rental price for {car.brand} {car.model}: ${car.set_rental_price_per_day(new_price)}/day")
        


    elif choice == "bike":
        bike_types()
        print()
        bike_num = input("please Enter the number of the car that you want to rent: ")

        if bike_num == 1:
            show_vehicle_info(bike1)
        elif bike_num == 2:
            show_vehicle_info(bike2)
        elif bike_num == 3:
            show_vehicle_info(bike3)
        elif bike_num == 4:
            show_vehicle_info(bike4)
        else:
            print("please choose any number from the list!!")

        print("please enter how many days you want to rent this car: ")
        rental_days = int(input("days: "))
        print(f"Rental cost for {bike.brand} Corolla for {rental_days} days: {car}")
        
        print("Do you Suggest another price for this bike?")
        suggestion = input("Enter yes to change the price or no to keep it the same: ").lower()

        if suggestion == "yes":
            new_price = int(input("Enter your suggestion price: "))
            if new_price > 0:
                print("Your suggestion can't be negative")
            else:
                print(f"Updated rental price for {bike.brand} {bike.model}: ${bike.set_rental_price_per_day(new_price)}/day")

    else:
        print("invalid choise. please enter 'Car' or 'Bike'!!")

#Design a Car Rental Management System using classes.


class Car:
    def __init__(self, name, number, price):
        self.name = name
        self.number = number
        self.price_per_day = price
        self.is_available = True

    def rent(self):
        if self.is_available == False:
            print("The car is already rented")
        else:
            self.is_available = False
            print("Car rented successfully")

    def return_car(self):
        if self.is_available == False:
            self.is_available = True
            print("Car returned successfully")
        else:
            print("This car was not rented")

    def display_info(self):
        if self.is_available == True:
            print(f"{self.name} is available")


class RentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_available_cars(self):
        for car in self.cars:
            if car.is_available == True:
                print(f"{car.name} ({car.number}) is available")

    def rent_car(self, number):
        for car in self.cars:
            if car.number == number:
                if car.is_available == True:
                    car.is_available = False
                    print("Car rented successfully")
                else:
                    print("Car is already rented")
                return
        print("Car number not found")

    def return_car(self, number):
        for car in self.cars:
            if car.number == number:
                if car.is_available == False:
                    car.is_available = True
                    print("Car returned successfully")
                else:
                    print("This car was not rented")
                return
        print("Car number not found")


# -------- Main Program --------
system = RentalSystem()

c1 = Car("Toyota Innova", "TN10A1234", 2000)
c2 = Car("Hyundai i20", "TN59B7788", 1200)
c3 = Car("Honda City", "TN99C9090", 2500)

system.add_car(c1)
system.add_car(c2)
system.add_car(c3)

print("\n--- Available Cars ---")
system.show_available_cars()

number = input("\nEnter car number to rent: ")
system.rent_car(number)

number = input("\nEnter car number to return: ")
system.return_car(number)


       




            
            

              

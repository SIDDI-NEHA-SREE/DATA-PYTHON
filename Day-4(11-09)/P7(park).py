'''Smart Parking System:
• Create classes Vehicle, ParkingSpot, and ParkingLot.
• Create multiple objects (vehicles, spots, parking lot).
• Demonstrate object creation, attribute initialization, and method calls.
• Make sensitive attributes private (e.g., license plate, owner name, spot status).
• Provide getter/setter methods to access/update them safely.
• Show that direct access fails but methods work.
• Vehicle is the base class.
• Derived classes:
Bike (extra attribute: helmet_required)
Car (extra attribute: seats)
SUV (extra attribute: four_wheel_drive)
Truck (extra attribute: max_load_capacity)
• Each child class overrides display() to print its own details.
• Create a list of different vehicle objects (Bike, Car, SUV, Truck).
• Iterate and call display() → each object responds differently.
• Implement a calculate_parking_fee() method:
Bike → ₹20/hour
Car → ₹50/hour
SUV → ₹70/hour
Truck → ₹100/hour
• Demonstrate runtime polymorphism by calling the method on different objects.
• Create an abstract class/interface Payment (using abc module).
• Define an abstract method process_payment(amount).
• Create child classes:
CashPayment
CardPayment
UPIPayment
• Demonstrate abstraction by processing payments differently (just print “Paid ₹X via UPI”).
Task 1: Vehicle Classes
Implement base and derived vehicle classes with encapsulation.
Override display() and calculate_parking_fee().
Task 2: ParkingSpot Class
Implement ParkingSpot with size restrictions (S, M, L, XL).
Methods: assign_vehicle(), remove_vehicle().
Ensure vehicle type fits correct spot size (Bike → S+, Car → M+, SUV → L+, Truck → XL only).
Task 3: ParkingLot Class
Store multiple parking spots.
Methods:
add_spot() → add new parking spots.
show_spots() → display all spots and their status.
park_vehicle(vehicle) → find suitable spot and park.
unpark_vehicle(vehicle) → remove from spot and calculate fee.
Task 4: Payment (Abstraction + Polymorphism)
When un-parking a vehicle, calculate fee (based on hours).
Ask user for payment method → process payment using appropriate child class.
Task 5: Main Program
Create a parking lot with mixed spots.
Create multiple vehicle objects.
Park/unpark vehicles.
Demonstrate encapsulation, inheritance, polymorphism, and abstraction throughout.'''
from abc import ABC, abstractmethod
class Vehicle:
    def __init__(self, license, name):
        self.__license = license  
        self.__name = name 

    def getlicense(self):
        return self.__license

    def setlicense(self, plate):
        self.__license = plate

    def getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name

    def display(self):
        print(f"Vehicle [License: {self.__license}, Owner: {self.__name}]")

    def calculate_parking_fee(self, hours):
        return 0


class Bike(Vehicle):
    def __init__(self, license, name, helmet=True):
        super().__init__(license, name)
        self.helmet = helmet

    def display(self):
        print(f"Bike [License: {self.get_license()}, Owner: {self.get_name()}, Helmet: {self.helmet}]")

    def calculate_parking_fee(self, hrs):
        return f"Bike -> ₹{20 * hrs}"


class Car(Vehicle):
    def __init__(self, license, name, seats=4):
        super().__init__(license, name)
        self.seats = seats

    def display(self):
        print(f"Car [License: {self.getlicense()}, Owner: {self.getname()}, Seats: {self.seats}]")

    def calculate_parking_fee(self, hrs):
        return f"Car -> ₹{50 * hrs}"


class SUV(Vehicle):
    def __init__(self, license, name, four_wheel_drive=True):
        super().__init__(license, name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print(f"SUV [License: {self.getlicense()}, Owner: {self.getname()}, 4WD: {self.four_wheel_drive}]")

    def calculate_parking_fee(self, hours):
        return f"SUV -> ₹{70 * hrs}"


class Truck(Vehicle):
    def __init__(self, license, name, max_load_capacity=1000):
        super().__init__(license, name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print(f"Truck [License: {self.getlicense()}, Owner: {self.getname()}, Max Load: {self.max_load_capacity}kg]")

    def calculate_parking_fee(self, hrs):
        return f"Truck -> ₹{100 * hrs}"
    
class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.__size = size            
        self.__occupied = False       

    def get_status(self):
        return self.__occupied

    def assign_vehicle(self, vehicle):
        if not self.__occupied:
            if isinstance(vehicle, Bike) and self.__size in ["S", "M", "L", "XL"]:
                self.__vehicle = vehicle
                self.__occupied = True
                vehicle.entry_time = datetime.datetime.now()
                return True
            elif isinstance(vehicle, Car) and self.__size in ["M", "L", "XL"]:
                self.__vehicle = vehicle
                self.__occupied = True
                vehicle.entry_time = datetime.datetime.now()
                return True
            elif isinstance(vehicle, SUV) and self.__size in ["L", "XL"]:
                self.__vehicle = vehicle
                self.__occupied = True
                vehicle.entry_time = datetime.datetime.now()
                return True
            elif isinstance(vehicle, Truck) and self.__size == "XL":
                self.__vehicle = vehicle
                self.__occupied = True
                vehicle.entry_time = datetime.datetime.now()
                return True
        return False

    def remove_vehicle(self):
        if self.__occupied:
            vehicle = self.__vehicle
            self.__vehicle = None
            self.__occupied = False
            return vehicle
        return None

    def display_spot(self):
        status = "Occupied" if self.__occupied else "Free"
        print(f"Spot {self.spot_id} ({self.__size}) - {status}")

class Payment:
    def amount(self, amt):
        return f"Payment method not specified"

class CashPayment(Payment):
    def amount(self, amt):
        return (f"Paid ₹{amt} in cash")

class CardPayment(Payment):
    def amount(self, amt):
        return(f"Paid ₹{amt} using credit/debit card")

class UPIPayment(Payment):
    def amount(self, amt):
        return(f"Paid ₹{amt} using UPI")

v={1:'Bike',2:'Car',3:'SUV',4:'Truck'}
k=Vehicle()
for i in v.keys():
    if i==1:
        k.Bike('1234','mej')
    elif i==2:


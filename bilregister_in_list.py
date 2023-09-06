import random
from time import time
import string
from typing import Self


class Car:
    """
    this class represent a vehicle with a plate.
    """
    def __repr__(self) -> str:
        return self.license_plate

    def __init__(self, license_plate:str = None ):
        if license_plate is None:
            self.generate_license_plate()
        else:
            self.license_plate =license_plate 
    
    def generate_license_plate(self):
        random_number = random.randint(100, 999)
        random_latters = "".join([chr(random.randint(65, 90)) for _ in range(3)])
        self.license_plate = f"{random_latters}{random_number}".upper()

def find_car_by_license_plate(cars: list[Car],
                              license_plate: str) -> Car or None:
    searched_area = get_sublist_for_license_plate(cars, license_plate)
    for car in searched_area:
        if car.license_plate == license_plate:
            return car
    return None


def get_sublist_for_license_plate(cars: list[list[Car]],
                             license_plate: str)-> Car or None:
    return cars[string.ascii_uppercase.index(license_plate[0])]


def register_car(func, car, cars)-> None:
    sub_list_of_car = func
    sub_list_of_car.append(car)
    cars.append(sub_list_of_car)


if __name__ == "__main__":
    cars = []

    for latter in string.ascii_uppercase:
        cars.append([])

    for car in range(2):
        car = Car()
        sub_list_of_car = get_sublist_for_license_plate(cars, car.license_plate)
        sub_list_of_car.append(car)
        cars.append(sub_list_of_car)
    register = input("do y9ou want to register a car? ")
    if register == "Y" or register == "y":
        input = input("please enter your license plate: ")
        car = Car(input)
        register_car(get_sublist_for_license_plate(cars, car.license_plate), car, cars)

    print(f"Search result:{find_car_by_license_plate(cars, input)}")
       
 

        





    
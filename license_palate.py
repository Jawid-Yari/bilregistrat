from time import time
import random
import string

class Car:
    def __init__(self, license_palate: str = None):
        if license_palate is None:
            self.assign_random_lciense_palate()
        else:
            self.license_palate = license_palate


    def assign_random_lciense_palate(self):
        license_number = random.randint(111, 999)
        license_chars = " "
        for i in range (3):
            characters = random.choice(string.ascii_uppercase)
            license_chars += characters
        self.license_palate = f"{license_chars} {license_number}"

    def __repr__(self) -> str:
        return self.license_palate

def get_cars_by_license_plate(cars: list[Car],
                              license_plate: str) -> Car or None:
    for car in cars:
        if car.license_palate == license_plate:
            return car
        
    return None
    

if __name__ == "__main__":

    car = Car()
    print(f" Your license palate is:{car.license_palate}")
    one_milion_cars = [ ]
    for c in range(10**6):
        car = Car()
        one_milion_cars.append(car)

    print(f" Here is the list of all yors cars:{one_milion_cars[:10]}")
    start = time()
    print(get_cars_by_license_plate(one_milion_cars, license_plate= "HYT358"))
    end = time()
    print(f"It took {end-start} secounds to check.")
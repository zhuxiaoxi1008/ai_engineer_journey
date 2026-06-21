from enum import Enum

class CarType(str, Enum):
    SEDAN = "sedan"
    SUV = "suv"
    WAGON = "wagon"
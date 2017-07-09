# Define a class for my car

class Car(object):
    # implement the car object.
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.engineSize = ''

    

class ElectricCar(Car):

    def __init__(self):
        Car.__init__(self)

    

class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)

    

class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)

    


class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)

    





class CarFleet(object):

    def __init__(self):
        self.__cars = []
        self.__numAvailable = 40
        self.__profit = 0.0

    def getNumAvailable(self):
        return self.__numAvailable

    def rentCar(self, numCars):
        self.__numAvailable -= numCars

    def returnCar(self, numCars):
        self.__numAvailable += numCars
        
        
        
        
        
        
        


        

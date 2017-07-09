print "Welcome to DBS CarRental. "

from CarRental import Car, ElectricCar, PetrolCar, DieselCar, HybridCar


class CarRental(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []

    def create_current_stock(self):
        for i in range(20):
           self.petrol_cars.append(PetrolCar())
        for i in range(8):
           self.diesel_cars.append(DieselCar())
        for i in range(4):
            self.electric_cars.append(ElectricCar())
        for i in range(8):
            self.hybrid_cars.append(HybridCar())

   
        

    def stock_count(self):
        print 'petrol cars left in stock ' + str(len(self.petrol_cars))
        print 'electric cars left in stock ' + str(len(self.electric_cars))
        print 'diesel cars left in stock ' + str(len(self.diesel_cars))
        print 'hybrid cars left in stock ' + str(len(self.hybrid_cars))

    

    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print 'Sorry nothing to rent, please try again'
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1

    

    def process_rental(self):
        answer = raw_input('would you like to rent a car? y/n: ')
        if answer == 'y':
            answer = raw_input('what type would you like? Electric, Petrol, Diesel or Hybrid?: ')
            amount = int(raw_input('how many would you like? '))
            if answer == 'p':
                self.rent(self.petrol_cars, amount)
            if answer == 'e':
                self.rent(self.electric_cars, amount)
            if answer == 'd':
                self.rent(self.diesel_cars, amount)
            if answer == 'h':
                self.rent(self.hybrid_cars, amount)

    

    

 
            
        self.stock_count()

carrental = CarRental()
carrental.create_current_stock()
proceed = 'y'
while proceed == 'y':
    carrental.process_rental()
    proceed = raw_input('continue? y/n: ')







import unittest

from CarRental import Car, ElectricCar, PetrolCar, DieselCar, HybridCar, CarFleet

# test the car functionality
class TestCar(unittest.TestCase):

    

    def test_car_fleet(self):
        car_fleet = CarFleet()

        self.assertEqual(40, car_fleet.getNumAvailable())


        car_fleet.rentCar(5)
       
        self.assertEqual(35, car_fleet.getNumAvailable())


        car_fleet.returnCar(2)
        self.assertEqual(37, car_fleet.getNumAvailable())


        car_fleet.returnCar(3)
        self.assertEqual(40, car_fleet.getNumAvailable())

        car_fleet.returnCar(3)
        car_fleet.rentCar(50)

if __name__ == '__main__':
    unittest.main()

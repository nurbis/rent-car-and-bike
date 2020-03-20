#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 00:21:00 2020

@author: nurbanuozkan
"""


class vehicleRent: #parent class
    def __init__(self , stock):
        self.stock=stock
        self.now=0
    def displayStock(self):
        print("{} vehicle are in stock".format(self.stock))
        return self.stock
    def rentHourly(self,n):
        if n<1:
            print("number of rented car will be positive.")
        elif n>self.stock:
            print("{} vehicle are in stock".format(self.stock))
        else :
            self.stock-=n
            self.now=datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours".format(n,self.now.hour))
        return self.now
    def rentDaily(self,n):
        if n<1:
            print("number of rented car will be positive.")
        elif n>self.stock:
            print("{} vehicle are in stock".format(self.stock))
        else :
            self.stock-=n
            self.now = datetime.datetime.now()
            print("{} vehicle are rented for daily at {}".format(n,self.now.hour))
        return self.now
    def returnVehicle(self, request, brand):
        car_h_price=10
        car_d_price=car_h_price*8/10*24
        bike_h_price=5
        bike_d_price=bike_h_price*7/10*24
        
        bill=0
        
        rentalTime, rentalBasis, numofVehicle = request
        
        if brand =="car":
            if rentalTime and rentalBasis and numofVehicle:
                self.stock += numofVehicle
                now = datetime.datetime.now()
                timeDifferences=rentalTime-now
                
                if rentalBasis==1: #(hourly)
                    bill= car_h_price*timeDifferences.seconds/3600*numofVehicle
                elif rentalBasis==2: #(daily)
                    bill= car_d_price*timeDifferences.seconds/3600*numofVehicle
                if numofVehicle>2:
                    print("you have %20 discount")
                    bill -= bill*0.2
                print("thank you, you rented {} car for {} time. your bill is {} ".format(numofVehicle,timeDifferences,bill))
                return bill
        elif brand =="bike":
            if rentalTime and rentalBasis and numofVehicle:
                self.stock += numofVehicle
                now = datetime.datetime.now()
                timeDifferences=rentalTime-now
                
                if rentalBasis==1: #(hourly)
                    bill= bike_h_price*timeDifferences.seconds/3600*numofVehicle
                elif rentalBasis==2: #(daily)
                    bill= bike_d_price*timeDifferences.seconds/3600*numofVehicle
                if numofVehicle>2:
                    print("you have %20 discount")
                    bill -= bill*0.2
                print("thank you, you rented {} bike for {} time. your bill is {} ".format(numofVehicle,timeDifferences,bill))
                return bill
        else:
            print("error")
            return None
class carRent(vehicleRent):
    global discountRate
    discountRate = 15
    def __init__(self, stock):
        super().__init__(stock)
    
    def discount(self, b):
        bill=b - (b*discountRate/100)
        return bill

class bikeRent(vehicleRent):
    def __init__(self, stock):
        super().__init__(stock)

class customer:
    def __init__(self):
        self.rentalTime_c=0
        self.rentalBasis_c=0
        self.numofVehicleCars=0
        
        self.rentalTime_b=0
        self.rentalBasis_b=0
        self.numofVehicleBikes=0
        
    def requestVehicle(self, brand):
        if brand=="bike":
            bikes=input("how many bikes would you like to rent?")
                
            try:
                bikes=int(bikes)
            except ValueError: 
                print("it must be number")
                return -1
            if bikes<1:
                print("it must be greater than zero")
            else:
                self.numofVehicleBikes=bikes
            return self.numofVehicleBikes
        if brand=="car":
            bikes=input("how many cars would you like to rent?")
                
            try:
                cars=int(cars)
            except ValueError: 
                print("it must be number")
                return -1
            if cars<1:
                print("it must be greater than zero")
            else:
                self.numofVehicleCars=cars
            return self.numofVehicleCars
    def returnVehicle(self, brand):
        if brand=="bike":
            if self.rentalTime_b and self.rentalBasis_b and self.numofVehicleBikes:
                return self.rentalTime_b, self.rentalBasis_b, self.numofVehicleBikes
            else:
                return 0,0,0
        if brand=="car":
            if self.rentalTime_c and self.rentalBasis_c and self.numofVehicleBikes:
                return self.rentalTime_c, self.rentalBasis_c, self.numofVehicleBikes
            else:
                return 0,0,0          



bike=bikeRent(100)
car=carRent(10)
customer=customer()

main_menu=True
while True:
    if main_menu:
        print("""
                  ***** Vehicle Rental Shop*****
                  A. Bike Menu
                  B. Car Menu
                  Q. Exit
                  """)
        main_menu = False
        choice=input("Enter choice")
    if (choice=="A"):
        
        print("""
              ****** BIKE MENU*****
              1. Display available bikes
              2. Request a bike on hourly basis $ 5
              3. Request a bike on daily basis $ 84
              4. Return a bike
              5. Main Menu
              6. Exit
              """)
        choice=input("Enter choice: ")
        try:
            choice=int(choice)
        except ValueError:
            print("hata")
            continue
            
        if choice== 1:
            bike.displayStock()
            choice="A"
            
        elif choice== 2:
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            
        elif choice== 3:
            bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b= 2
            
        elif choice== 4:
            bike.returnVehicle(customer.returnVehicle("bike"), "bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            
        elif choice == 5:
            main_menu = True
            
        elif choice ==6:
            break
            
        else:
            print("Invalid input. Please enter a number between 1-6 ")
            main_menu = True
    if (choice=="B"):
        print("""
              ****** CAR MENU*****
              1. Display available cars
              2. Request a car on hourly basis $ 5
              3. Request a car on daily basis $ 84
              4. Return a car
              5. Main Menu
              6. Exit
              """)
        choice = input("Enter choice: ")
        try:
            choice=int(choice)
        except ValueError:
            print("hata")
            continue
            
        if choice== 1:
            car.displayStock()
            choice="B"
            
        elif choice== 2:
            customer.rentalTime_b = car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis_b = 1
            
        elif choice== 3:
            car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasis_b= 2
            
        elif choice== 4:
            car.returnVehicle(customer.returnVehicle("car"),"car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            
        elif choice == 5:
            main_menu = True
            
        elif choice ==6:
            break
            
        else:
            print("Invalid input. Please enter a number between 1-6 ")
            main_menu = True
            
    elif choice == "Q" or choice == "q":  
        break
        
    else:
        print("Invalid Input. Please Enter A-B-Q")
        main_menu = True
    print("Thank you for using the vehicle rental shop")
            
        
    
        











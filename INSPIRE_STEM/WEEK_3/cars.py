# this is a class that describes cars
# date : 1/03/2024
# name : Rozina Adhiambo

#initializing the car
class car:
    def __init__ (self, model,make,year_of_production, fuel_capacity , colour, horse_power):
        self.model = model 
        self.make = make
        self.year_of_production = year_of_production
        self.fuel_capacity = fuel_capacity
        self.colour = colour
        self.horse_power = horse_power

# creating a function to print the horse power
    def print_make(self,make):
        print("The car is of {0} make.". format(self.make))

#difference between setting and getting
    def set_make(self,make):# takes 2 parameters: self and whatever you want to set
        self.make = make

    def get_make(self): # when using get you only need one parameter
        return self.make
    
    def set_colour(self,colour):# takes 2 parameters: self and whatever you want to set
        self.make = colour

    def get_colour(self): # when using get you only need one parameter
        return self.colour


     
my_car = car ("Impalla","Chevrolet", "1969","2500cc","lillac"," 390 hp")

friends_car = car("Note","Nissan", "2014","1400cc","black "," 300 hp")

my_car.print_make("Chevrolet")

#setting the makes
my_car.set_make("Ford")
friends_car.set_make("Toyota")

#getting the makes

print(my_car.get_make())
print(friends_car.get_make())

#printing the makes


#setting the makes
my_car.set_colour("Grey")
friends_car.set_colour("Blue")

#getting the makes

print(my_car.get_colour())
print(friends_car.get_colour())





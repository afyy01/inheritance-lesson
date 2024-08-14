#inheritance - having a child class with some properties or some attributes of parent class
#parent class 
class Car: 
    #constructor
    def __init__(self,brand,model,color,fuel):
        self.brand = brand
        self.model = model 
        self.color = color
        self.fuel = fuel
    
    #getter method
    def get_color(self):
        return self.color 
    
    #setter method 
    def set_color(self,new_color):
        self.color = new_color

    #custom function
    def showCar(self):
        print("This is a car of {} brand of model no. {} with the color {} and taking the {}".format(self.brand,self.model,self.color,self.fuel))
              
#child class
class SUV(Car):
    def __init__ (self,brand,model,color,fuel,turbo):
            self.turbo= turbo
            Car.__init__(self,brand,color,model,fuel)

    def showCar(self):
        print("This is a car of {} brand of model no. {} with the color {} and taking the {} with the turbo as {}".format(self.brand,self.model,self.color,self.fuel,self.turbo))
              

#object
audi = SUV("audi","Q3", "Black", "100fuel","True")
audi.showCar()

print(audi.get_color())

audi.set_color("blue")
audi.showCar()
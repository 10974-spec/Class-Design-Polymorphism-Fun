class Car:  
    def move(self):  
        print("Vroom! Driving on highways")  

class Plane:  
    def move(self):  
        print("Whoosh! Flying above clouds")  

class Submarine:  
    def move(self):  
        print("Glub! Diving underwater")  

# Let them move!  
vehicles = [Car(), Plane(), Submarine()]  
for vehicle in vehicles:  
    vehicle.move()  

# Output:  
# Vroom! Driving on highways  
# Whoosh! Flying above clouds  
# Glub! Diving underwater

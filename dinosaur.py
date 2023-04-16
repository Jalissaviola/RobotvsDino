

class Dinosaur: 


    def __init__(self,name,attack_power):
        self.name= name 
        self.health= 100
        self.attack=attack_power 

     #This attack method should lower a Robot’s health
     #  by the value of the Dinosaur’s attack_power. 
     
    def attack_robot(self,robot_obj): 
        robot_obj.health -= self.attack 
        
        


       

     

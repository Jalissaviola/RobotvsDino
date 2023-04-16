from weapon import Weapon 

class Robot: 

    def __init__(self,name):
        self.name=name 
        self.health= 100
        self.active_weapon= Weapon("Cybersword",15)

    #This attack method should lower the Dinosaur’s health 
    # by the attack_power of the Robot’s active_weapon.
    
    def attack_dinosaur(self,dino_obj):
        
        dino_obj.health -= self.active_weapon.attack_power


    




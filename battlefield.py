from dinosaur import Dinosaur
from robot import Robot 

class Battlefield:

    def __init__(self):
        self.robot=Robot("CyberFlex")
        self.dinosaur= Dinosaur("Godzilla",10)

    def run_game(self):
        Battlefield.display_weclcome(self)
        self.robot.attack_dinosaur(self.robot)
        self.dinosaur.attack_robot(self.dinosaur)
        Battlefield.battle_phase(self)
        Battlefield.display_winner(self)


    def display_weclcome(self):
        print("\n")
        print("\nWELCOME TO A GAME OF ROBOT VS. DINOSAUR!")
        print("\tMay the Best Player WIN !!!")
        print("\n")

    def battle_phase(self):

        while self.robot.health  > 0 and self.dinosaur.health > 0:
            self.dinosaur.health -= self.robot.active_weapon.attack_power
            print('Robot CyberFlex attacked Godzilla with a cybersword for 15 damages!')
            print(f'- Godzilla has {self.dinosaur.health} health remaining')
            print("\n")
            if self.dinosaur.health >0: 
                    self.robot.health -= self.dinosaur.attack_power  
                    print("Godzilla attacked Robot CyberFlex for 10 damages! ")
                    print(f'-Robot CyberFlex has {self.robot.health} health remaining')
                    print("\n")

            

    def display_winner(self):
       
        while True:
            if self.dinosaur.health == 0: 
                print("Godzilla was extinct!")
                print("Robot CyberFlex for the Win!!!!")
                print('\n')
                break
                
            elif self.robot.health== 0:
                print("Robot CyberFLex was disconnected!")
                print("Godzilla for the win!")
                print("\n")
                break  
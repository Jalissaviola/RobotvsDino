from dinosaur import Dinosaur
from robot import Robot 

class Battlefield:

    def __init__(self):
        self.robot=Robot("CyberFlex")
        self.dinosaur= Dinosaur("Godzilla","10")

    def run_game(self):
        Battlefield.display_weclcome(self)
        Battlefield.battle_phase(self)
        self.robot.attack_dinosaur(self.robot)
        self.dinosaur.attack_robot(self.dinosaur)


    def display_weclcome(self):
        print("WELCOME TO A GAME OF ROBOT VS. DINOSAUR!")
        print("May the Best Player WIN !!!")

    def battle_phase(self):
        pass 

    def display_winner(self):
        pass 
class RugbyPlayer:  
    def __init__(self, name, position):  
        self.name = name  # 🏷 Player name  
        self.position = position  #  Playing position  

    def play_position(self):  
        print(f"{self.name} is playing as {self.position}! ")  

#  Child class  
class TeamCaptain(RugbyPlayer):  
    def __init__(self, name, position, team):  
        super().__init__(name, position)  
        self.team = team  # 🏆 Which team they captain  

    def motivate_team(self):  
        print(f"{self.name} shouts: 'Tuko pamoja {self.team}!' ")  

#  Create players  
collins = RugbyPlayer("Collins Injera", "Winger")  
andrew = TeamCaptain("Andrew Amonde", "Flanker", "Shujaa")  

collins.play_position()   
andrew.motivate_team()

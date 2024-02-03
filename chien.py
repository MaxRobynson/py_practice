class Chien():
    def __init__(self, race, color, genre):
        self.race = race
        self.color = color
        self.genre = genre

    def aboyement(self):
        return "Woaff woaff !!"
    def manger(self):
        return "miaam miaam"

class Cat(Chien):
    super(self.__init__)
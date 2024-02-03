class Bird:
    def __init__(self) -> None:
        # Attributs d'instance
        self.wings = 2
        
    def fly(self):
        #Mrthode d'instance
        print("i lfly")
        
bird = Bird()#obliger d'instancier un oeiseau pour ulitlesr les attributs
bird.wings
bird.fly()


class Bird1:
    # ici on utlise les c
    names = ('mouette', 'pigeon', 'moineau', 'hirrondelle')
    positions = {}
    
    def __init__(self, name):
        self.postion = 1, 2
        self.name = name
    
        #on accede a l'attributs de classe 'positions' avec self
        self.positions[self.postion] = self.name
    
    @classmethod
    def find_bird(cls, position):
        if position in cls.positions:
            return f'On a trouve un {cls.positions[position]}'
        return 'On a rien trouver'
    
#On accede aux varaibles de classe sans instanciation
Bird1.names
Bird1.positions
print(Bird1.find_bird((2, 5)))

#on instancie n oiseau
birdd = Bird1("mouette")
print(Bird1.find_bird((1, 2)))


class Bird2:
    @staticmethod
    def get_definition():
        """Donne la definition d'un oiesea"""
        return ("bla bla bla")
    
print(Bird2.get_definition())
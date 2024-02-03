class Toolbox:
    """boite a outils"""
    def __init__(self):
        self.tools = []
    def add_tool(self, tool):
        self.tools.append(tool)
        
        
    def remove_tool(self, tool):
        index = self.tools.index(tool)
        del self.tools[index]
    
class Screwdriver:
    """tournevisi"""
    def __init__(self, size):
        self.size = size
    def tighten(self, screw):
        """serrer un vis"""
        screw.tighten()
        
    def loosen(self, screw):
        """desserre un vis"""
        screw.loosen()
        
    def __repr__(self) -> str:
        """Representation de l'objet"""
        return f'Tournevis de taille {self.size}'
    
class Hammer:
    def __init__(self, color='red'):
        self.color = color
        
    def paint(self, color):
        self.color = color
    
    def hammer_in(self, nail):
        """enfoce un clou"""
        nail.nail_in()
    
    def remove(self, nail):
        """enleve un clou"""
        nail.remove()
        
    def __repr__(self) -> str:
        return f'Marteau de couleur {self.color}'
    
class Screw:
    """vis"""
    MAX_TIGHTNESS = 5
    def __init__(self):
        self.tightness = 0
    
    def loosen(self):
        if self.tightness > 0:
            self.tightness -=1
    
    def tighten(self):
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness +=1
    
    def __str__(self) -> str:
        return "Vis avec un serrage de {}".format(self.tightness)
    
class Nail:
    """ Clou"""
    def __init__(self) -> None:
        self.in_wall = False
    
    def nail_in(self):
        if not self.in_wall:
            self.in_wall = True
    
    def remove(self):
        if self.in_wall:
            self.in_wall = False
        
    def __str__(self) -> str:
        wall_state = "dans le mur" if self.in_wall else "hors du mur" 
        return f'Clou {wall_state}'       
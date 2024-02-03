class Individul:
    def __init__(self, character_name: str) -> None:
        self.character_name = character_name
        self.happy = True
    
    def get_character_name(self):
        return self.character_name
    
    def is_happy(self):
        return self.happy
    
    def switch_mood(self):
        self.happy = False
        return self.happy
    def speak(self):
        if self.happy :
            return f'Hello, i am {self.character_name}'
        else:
            return 'Go away'

individual1 = Individul('Buster')
individual2 = Individul('Tobias')
print(individual1.get_character_name(), individual2.get_character_name())
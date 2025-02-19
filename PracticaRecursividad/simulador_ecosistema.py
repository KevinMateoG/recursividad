class presa:
    def __init__(self, animal_presa):
        self.animal_presa: str = animal_presa
        self.energia: int = 50

    def alimentarse(self):
        pass
    
    def __str__(self):
        return self.animal

class depredador:
    def __init__(self, animal_depredador):
        self.animal_depredador: str = animal_depredador
        self.energia: int = 50
    
    def alimentarse(self):
        pass
    
    def __str__(self):
        return self.animal_depredador
    

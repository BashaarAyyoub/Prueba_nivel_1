class vehicle():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __name__(self):
        return self.__class__.__name__ 
    
    def __catalogar__(vehicles):
        for vehicle in vehicles:
            print(type(vehicle).__name__,vehicle)
        
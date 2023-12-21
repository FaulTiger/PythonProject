import Pump
class Container(Pump):
    
    def __init__(self,name, content, contentsize,pump):
        self.name = name
        self.content = content
        self.contentsize = contentsize
        self.pump = Pump.Pump(pump)
        
    def fillFromContainer(self,amount):
        #Berechnung für Pumpzeit
        self.pump.activatepump(self.pump,amount)
from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, name:str, battery_level=100, status="idle"): 
        self._name = name
        self._battery_level = battery_level 
        self._status = status
        
    def get_name(self):
        return self._name
    
    def get_battery_level(self):
        return self._battery_level
    
    def get_status(self):
        return self._status
        
    def charge(self):
        self._battery_level = 100
        self._status = "charging"
        print("I'm charging ...")
    
    @abstractmethod
    def work(self):
        pass
    
    def report_status(self):
        print(self.get_name() + " | Status: " + self.get_status() + " | Battery Level: " + str(self.get_battery_level()))
        
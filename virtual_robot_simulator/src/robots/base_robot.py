from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, name:str, battery_level:int, status:str): 
        self._name = name
        if battery_level > 100:
            self._battery_level = 100
        elif battery_level < 0:
            self._battery_level = 0
        else:
            self._battery_level = battery_level 
        self._status = status
        
    def get_name(self) -> str:
        return self._name
    
    def get_battery_level(self) -> int:
        return self._battery_level
    
    def get_status(self) -> str:
        return self._status
        
    def charge(self) -> None:
        self._battery_level = 100
        self._status = "charging"
        print("I'm charging ...")
    
    @abstractmethod
    def work(self) -> None:
        pass
    
    def report_status(self) -> None:
        print(self.get_name() + " | Status: " + self.get_status() + " | Battery Level: " + str(self.get_battery_level()))
        
    @classmethod        
    def class_diagnostic_info(cls) -> str:
        return f"{cls.__name__} diagnostic: Check all systems."
    
    @staticmethod
    def static_diagnostic_info() -> str:
        return "Ensure the robot is charged and in good condition."
    
    @staticmethod
    def is_valid_battery(battery:int) -> bool:
        return (0 <= battery) and (100 >= battery)
    
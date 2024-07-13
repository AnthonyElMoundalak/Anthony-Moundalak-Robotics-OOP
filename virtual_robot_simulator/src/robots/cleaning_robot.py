from .base_robot import Robot

class CleaningRobot(Robot):
    def __init__(self, name:str, battery_level, status, cleaning_tool:str):
        super().__init__(name, battery_level, status)
        self._cleaning_tool = cleaning_tool
        
    def get_tool(self):
        return self._cleaning_tool
        
    def work(self):
        if self._battery_level >= 20:
            self._battery_level -= 20
            self._status = "working"
            print("I'm cleaning with " + self._cleaning_tool + "...")
        else:
            print(self.get_name() + " has insufficient battery to clean")
            
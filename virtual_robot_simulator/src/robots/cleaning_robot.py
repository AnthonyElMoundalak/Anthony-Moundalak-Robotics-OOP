from .base_robot import Robot

class CleaningRobot(Robot):
    def __init__(self, name:str, battery_level:int, status:str, cleaning_tool:str):
        Robot.__init__(self, name, battery_level, status)
        self._cleaning_tool = cleaning_tool
        
    def get_tool(self) -> str:
        return self._cleaning_tool
        
    def work(self) -> None:
        if self._battery_level >= 20:
            self._battery_level -= 20
            self._status = "working"
            print("I'm cleaning with " + self._cleaning_tool + "...")
        else:
            print(self.get_name() + " has insufficient battery to clean")
            
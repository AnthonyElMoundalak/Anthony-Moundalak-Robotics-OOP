from .base_robot import Robot

class CookingRobot(Robot):
    def __init__(self, name:str, battery_level:int, status:str, cooking_skill:str):
        Robot.__init__(self, name, battery_level, status)
        self._cooking_skill = cooking_skill
        
    def get_skill(self) -> str:
        return self._cooking_skill
        
    def work(self) -> None:
        if self._battery_level >= 30:
            self._battery_level -= 30
            self._status = "working"
            print("I'm cooking as a " + self._cooking_skill + " chef...")
        else:
            print(self.get_name() + " has insufficient battery to cook")
            
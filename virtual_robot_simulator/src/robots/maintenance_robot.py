from .cleaning_robot import CleaningRobot
from .cooking_robot import CookingRobot

class MaintenanceRobot(CleaningRobot, CookingRobot):
    def __init__(self, name: str, battery_level:int, status:str, cleaning_tool: str, cooking_skill: str):
        CleaningRobot.__init__(self, name, battery_level, status, cleaning_tool)
        CookingRobot.__init__(self, name, battery_level, status, cooking_skill)
        
    def multi_task(self) -> None:
        print(f"{self.get_name()} is starting multi-tasking...")
        CleaningRobot.work(self)  # Perform cleaning task
        if self.get_battery_level() > 30:  # Check if there's enough battery for the next task
            CookingRobot.work(self)  # Perform cooking task
        print(MaintenanceRobot.__mro__)
        
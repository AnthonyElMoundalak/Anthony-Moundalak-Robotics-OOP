from .cleaning_robot import CleaningRobot
from .cooking_robot import CookingRobot

class MaintenanceRobot(CleaningRobot, CookingRobot):
    """
    A subclass of CleaningRobot and CookingRobot representing a Maintenance Robot capable of multi-tasking.
    """
    
    def __init__(self, name: str, battery_level:int, status:str, cleaning_tool: str, cooking_skill: str):
        """
        Initializes the MaintenanceRobot with the given name, battery level, status, cleaning tool, and cooking skill.
        
        Args:
            name (str): The name of the maintenance robot.
            battery_level (int): The initial battery level of the maintenance robot.
            status (str): The initial status of the maintenance robot.
            cleaning_tool (str): The cleaning tool used by the robot.
            cooking_skill (str): The cooking skill possessed by the robot.
        """
        CleaningRobot.__init__(self, name, battery_level, status, cleaning_tool)
        CookingRobot.__init__(self, name, battery_level, status, cooking_skill)
        
    def multi_task(self) -> None:
        """
        Performs multi-tasking by first cleaning and then, if sufficient battery remains, cooking.
        
        Prints:
            Messages indicating the robot is performing cleaning and cooking tasks.
        """
        print(f"{self.get_name()} is starting multi-tasking...")
        CleaningRobot.work(self)  # Perform cleaning task
        if self.get_battery_level() > 30:  # Check if there's enough battery for the next task
            CookingRobot.work(self)  # Perform cooking task
        print(MaintenanceRobot.__mro__)
        
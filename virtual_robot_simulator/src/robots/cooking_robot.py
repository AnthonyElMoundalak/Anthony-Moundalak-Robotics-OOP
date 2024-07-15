from .base_robot import Robot

class CookingRobot(Robot):
    """
    A subclass of Robot representing a Cooking Robot with an additional cooking skill attribute.
    
    Attributes:
        _cooking_skill (str): The cooking skill of the robot.
    """
    
    def __init__(self, name:str, battery_level:int, status:str, cooking_skill:str):
        """
        Initializes the CookingRobot with the given name, battery level, status, and cooking skill.
        
        Args:
            name (str): The name of the cooking robot.
            battery_level (int): The initial battery level of the cooking robot.
            status (str): The initial status of the cooking robot.
            cooking_skill (str): The cooking skill possessed by the robot.
        """
        Robot.__init__(self, name, battery_level, status)
        self._cooking_skill = cooking_skill
        
    def get_skill(self) -> str:
        """
        Returns the cooking skill possessed by the robot.
        
        Returns:
            str: The cooking skill of the robot.
        """
        return self._cooking_skill
        
    def work(self) -> None:
        """
        Performs cooking work if the battery level is sufficient. Decreases the battery level by 30 units.
        
        Prints:
            A message indicating the robot is cooking with its specific cooking skill if the battery level is sufficient.
            A message indicating insufficient battery if the battery level is below 30 units.
        """
        if self._battery_level >= 30:
            self._battery_level -= 30
            self._status = "working"
            print("I'm cooking as a " + self._cooking_skill + " chef...")
        else:
            print(self.get_name() + " has insufficient battery to cook")
            
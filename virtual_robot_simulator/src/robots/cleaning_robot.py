from .base_robot import Robot

class CleaningRobot(Robot):
    """
    A subclass of Robot representing a Cleaning Robot with an additional cleaning tool attribute.
    
    Attributes:
        _cleaning_tool (str): The tool used by the cleaning robot.
    """
    
    def __init__(self, name:str, battery_level:int, status:str, cleaning_tool:str):
        """
        Initializes the CleaningRobot with the given name, battery level, status, and cleaning tool.
        
        Args:
            name (str): The name of the cleaning robot.
            battery_level (int): The initial battery level of the cleaning robot.
            status (str): The initial status of the cleaning robot.
            cleaning_tool (str): The cleaning tool used by the robot.
        """
        Robot.__init__(self, name, battery_level, status)
        self._cleaning_tool = cleaning_tool
        
    def get_tool(self) -> str:
        """
        Returns the cleaning tool used by the robot.
        
        Returns:
            str: The cleaning tool of the robot.
        """
        return self._cleaning_tool
        
    def work(self) -> None:
        """
        Performs cleaning work if the battery level is sufficient. Decreases the battery level by 20 units.
        
        Prints:
            A message indicating the robot is cleaning if the battery level is sufficient.
            A message indicating insufficient battery if the battery level is below 20 units.
        """
        if self._battery_level >= 20:
            self._battery_level -= 20
            self._status = "working"
            print("I'm cleaning with " + self._cleaning_tool + "...")
        else:
            print(self.get_name() + " has insufficient battery to clean")
            
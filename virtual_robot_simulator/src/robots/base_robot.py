from abc import ABC, abstractmethod

class Robot(ABC):
    """
    An abstract base class representing a Robot with basic attributes and functionalities.
    
    Attributes:
        _name (str): The name of the robot.
        _battery_level (int): The current battery level of the robot (0-100).
        _status (str): The current status of the robot.
    """
    
    def __init__(self, name:str, battery_level:int, status:str): 
        """
        Initializes the Robot with the given name, battery level, and status.
        
        Args:
            name (str): The name of the robot.
            battery_level (int): The initial battery level of the robot.
            status (str): The initial status of the robot.
        
        Notes:
            The battery level is clamped to the range [0, 100].
        """
        self._name = name
        if battery_level > 100:
            self._battery_level = 100
        elif battery_level < 0:
            self._battery_level = 0
        else:
            self._battery_level = battery_level 
        self._status = status
        
    def get_name(self) -> str:
        """
        Returns the name of the robot.
        
        Returns:
            str: The name of the robot.
        """
        return self._name
    
    def get_battery_level(self) -> int:
        """
        Returns the current battery level of the robot.
        
        Returns:
            int: The current battery level of the robot.
        """
        return self._battery_level
    
    def get_status(self) -> str:
        """
        Returns the current status of the robot.
        
        Returns:
            str: The current status of the robot.
        """
        return self._status
        
    def charge(self) -> None:
        """
        Charges the robot to full battery level and updates its status to 'charging'.
        
        Prints:
            A message indicating the robot is charging.
        """
        self._battery_level = 100
        self._status = "charging"
        print("I'm charging ...")
    
    @abstractmethod
    def work(self) -> None:
        """
        An abstract method to be implemented by subclasses representing the robot performing work.
        """
        pass
    
    def report_status(self) -> None:
        """
        Reports the current status and battery level of the robot.
        
        Prints:
            The name, status, and battery level of the robot.
        """
        print(self.get_name() + " | Status: " + self.get_status() + " | Battery Level: " + str(self.get_battery_level()))
        
    @classmethod        
    def class_diagnostic_info(cls) -> str:
        """
        Returns diagnostic information for the class.
        
        Returns:
            str: A diagnostic message for the class.
        """
        return f"{cls.__name__} diagnostic: Check all systems."
    
    @staticmethod
    def static_diagnostic_info() -> str:
        """
        Returns general diagnostic information for any robot.
        
        Returns:
            str: A general diagnostic message.
        """
        return "Ensure the robot is charged and in good condition."
    
    @staticmethod
    def is_valid_battery(battery:int) -> bool:
        """
        Checks if the given battery level is within the valid range (0-100).
        
        Args:
            battery (int): The battery level to check.
        
        Returns:
            bool: True if the battery level is valid, False otherwise.
        """
        return (0 <= battery) and (100 >= battery)
    
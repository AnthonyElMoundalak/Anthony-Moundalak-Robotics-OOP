# Virtual Robot Simulator

## Overview

This assignment is to create our own robot classes in python and testing them with pytest. The aim is to practice OOP concepts such as classes, inheritance, polymorphism, and encapsulation.

## Implementation

### Robot Classes

- **Base Class: Robot**
with an abstract method `work()`
- **Derived Classes: CleaningRobot, CookingRobot**

### Advanced OOP Concepts

#### Class Methods and Static Methods

- **Static Methods**: Static methods belong to the class and not to any specific instance. They do not modify the class or instance state and are used for utility functions. In our implementation, `static_diagnostic_info` provides general diagnostic information, and `is_valid_battery` checks if the battery level is within the valid range.

  ```python
  @staticmethod
  def static_diagnostic_info() -> str:
      return "Ensure the robot is charged and in good condition."

  @staticmethod
  def is_valid_battery(battery: int) -> bool:
      return (0 <= battery) and (100 >= battery)
    ```

- **Class Methods**: Class methods are bound to the class and not the instance. They can modify the class state that applies across all instances. In our implementation, `class_diagnostic_info` provides diagnostic information specific to the robot class.

    ```python
    @classmethod
    def class_diagnostic_info(cls) -> str:
        return f"{cls.__name__} diagnostic: Check all systems."
    ```
#### Abstract Base Classes (ABCs)

- **Abstract Methods**: These are methods declared in an abstract base class that must be implemented by any subclass. They ensure that specific methods are consistently implemented across all subclasses.

    ```python
    class Robot(ABC):
        @abstractmethod
        def work(self) -> None:
            pass
    ```

### MaintenanceRobot

The `MaintenanceRobot` class inherits from both `CleaningRobot` and `CookingRobot` and implements a `multi_task` method that allows the robot to perform a cleaning task followed by a cooking task.

#### Method Resolution Order (MRO)

- **MRO**:The order in which Python looks for a method or attribute in a hierarchy of classes. MRO ensures that methods are resolved correctly without conflicts. You can view the MRO using the `__mro__ `attribute:

    ```python
    print(MaintenanceRobot.__mro__)
    ```
For `MaintenanceRobot`, the MRO is:

    (<class 'maintenance_robot.MaintenanceRobot'>, <class 'cleaning_robot.CleaningRobot'>, <class 'cooking_robot.CookingRobot'>, <class 'base_robot.Robot'>, <class 'object'>)

This order ensures that methods from CleaningRobot and CookingRobot are called correctly.

### Testing Pytest:

Pytest is used for testing. It supports simple test functions and test classes, making it easy to ensure your code works correctly

## Usage

1. Clone the repository 
2. Enter to the repo directory
3. Build and run the docker image using docker-composer:

    ```python
    docker composer -up
import pytest
from ..maintenance_robot import MaintenanceRobot

@pytest.fixture
def robot():
    return MaintenanceRobot("MaintBot", 100, "idle", "vacuum", "intermediate")

def test_initialization(robot):
    assert robot.get_name() == "MaintBot"
    assert robot.get_battery_level() == 100
    assert robot.get_status() == "idle"
    assert robot.get_tool() == "vacuum"
    assert robot.get_skill() == "intermediate"
    
def test_multi_task(robot):
    robot.multi_task()
    assert robot.get_battery_level() == 50  # Cleaning (20) + Cooking (30)
    assert robot.get_status() == "working"

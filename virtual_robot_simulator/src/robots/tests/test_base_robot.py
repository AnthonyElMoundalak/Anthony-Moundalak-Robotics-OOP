import pytest
from ..base_robot import Robot

class TestRobotImplementation(Robot):
    def work(self):
        if self.get_battery_level() >= 10:
            self._battery_level -= 10
            self._status = "working"
        else:
            self._status = "idle"
        
@pytest.fixture
def robot():
    return TestRobotImplementation("TestBot", 100, "idle")

def test_initialization(robot):
    assert robot.get_name() == "TestBot"
    assert robot.get_battery_level() == 100
    assert robot.get_status() == "idle"

def test_charge(robot):
    robot._battery_level = 50
    assert robot.get_battery_level() == 50
    robot.charge()
    assert robot.get_battery_level() == 100
    assert robot.get_status() == "charging"

def test_report_status(robot, capsys):
    robot.report_status()
    captured = capsys.readouterr()
    assert "TestBot | Status: idle | Battery Level: 100" in captured.out
    
def test_work(robot):
    robot.work()
    assert robot.get_battery_level() == 90
    assert robot.get_status() == "working"

def test_static_method():
    assert Robot.static_diagnostic_info() == "Ensure the robot is charged and in good condition."
    assert Robot.is_valid_battery(78) == True
    assert Robot.is_valid_battery(178) == False
    assert Robot.is_valid_battery(-78) == False
    

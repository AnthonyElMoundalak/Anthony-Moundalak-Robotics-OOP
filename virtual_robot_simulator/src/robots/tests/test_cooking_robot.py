import pytest
from ..cooking_robot import CookingRobot

@pytest.fixture
def cook():
    return CookingRobot("CookingBot", 100, "idle", "expert")

def test_initialization(cook):
    assert cook.get_name() == "CookingBot"
    assert cook.get_battery_level() == 100
    assert cook.get_status() == "idle"
    assert cook.get_skill() == "expert"
    
def test_work(cook):
    cook.work()
    assert cook.get_battery_level() == 70
    assert cook.get_status() == "working"
    
def test_insufficient_battery(cook):
    cook._battery_level = 10
    cook.work()
    assert cook.get_battery_level() == 10
    assert cook.get_status() == "idle"

def test_charge(cook):
    cook._battery_level = 50
    assert cook.get_battery_level() == 50
    cook.charge()
    assert cook.get_battery_level() == 100
    assert cook.get_status() == "charging"
    
def test_report_status(cook, capsys):
    cook.report_status()
    captured = capsys.readouterr()
    assert "CookingBot | Status: idle | Battery Level: 100" in captured.out

def test_class_method():
    assert CookingRobot.class_diagnostic_info() == "CookingRobot diagnostic: Check all systems."



import pytest
from ..cleaning_robot import CleaningRobot

@pytest.fixture
def cleaner():
    return CleaningRobot("CleanerBot", 100, "idle", "vaccum")

def test_initialization(cleaner):
    assert cleaner.get_name() == "CleanerBot"
    assert cleaner.get_battery_level() == 100
    assert cleaner.get_status() == "idle"
    assert cleaner.get_tool() == "vaccum"
    
def test_work(cleaner):
    cleaner.work()
    assert cleaner.get_battery_level() == 80
    assert cleaner.get_status() == "working"
    
def test_insufficient_battery(cleaner):
    cleaner._battery_level = 10
    cleaner.work()
    assert cleaner.get_battery_level() == 10
    assert cleaner.get_status() == "idle"

def test_charge(cleaner):
    cleaner._battery_level = 50
    assert cleaner.get_battery_level() == 50
    cleaner.charge()
    assert cleaner.get_battery_level() == 100
    assert cleaner.get_status() == "charging"
    
def test_report_status(cleaner, capsys):
    cleaner.report_status()
    captured = capsys.readouterr()
    assert "CleanerBot | Status: idle | Battery Level: 100" in captured.out

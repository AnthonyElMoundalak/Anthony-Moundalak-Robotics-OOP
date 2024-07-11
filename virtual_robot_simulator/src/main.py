from robots.base_robot import Robot
from robots.cleaning_robot import CleaningRobot
from robots.cooking_robot import CookingRobot


cleaner = CleaningRobot("CleanerBot", 100, "idle","vaccum")
cook = CookingRobot("CookBot", 100, "idle", "expert")
    
cleaner.report_status()
cleaner.work()
cleaner.report_status()
cleaner.charge()
cleaner.report_status()
    
cook.report_status()
cook.work()
cook.report_status()
cook.charge()
cook.report_status()
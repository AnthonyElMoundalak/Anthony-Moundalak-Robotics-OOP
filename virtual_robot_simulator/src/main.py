from robots.base_robot import Robot
from robots.cleaning_robot import CleaningRobot
from robots.cooking_robot import CookingRobot
from robots.maintenance_robot import MaintenanceRobot


cleaner = CleaningRobot("CleanerBot", 100, "idle","vaccum")
cook = CookingRobot("CookBot", 100, "idle", "expert")
maintenance = MaintenanceRobot("MaintenanceBot", 100, "idle", "mop", "beginner")
    
print("cleaner")
print("------------------------------")
cleaner.report_status()
cleaner.work()
cleaner.report_status()
cleaner.charge()
cleaner.report_status()


print("------------------------------")
print("cooker")
print("------------------------------")    
cook.report_status()
cook.work()
cook.report_status()
cook.charge()
cook.report_status()


print("------------------------------")
print("maintenance")
print("------------------------------")  
maintenance.report_status()
maintenance.multi_task()
maintenance.report_status()
maintenance.charge()
maintenance.report_status()
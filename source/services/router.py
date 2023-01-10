from database import Database
from services.monitoring import MonitoringService


class Router:

    database = Database("test.db")
    working: bool = True
    monitoring_service = MonitoringService()


    def __init__(self):
        pass

    def write_metric(self):
        self.database.initialization()

        while self.working:
            a = self.monitoring_service.utilization(1)
            self.database.insert(a)
            print(a)



    def run(self):
        print("Metric Work!")
        self.write_metric()

    def stop(self):
        self.working = False
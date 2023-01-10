import time
import psutil
from models import Usage
from sqlite3 import Connection
from database import UsageDAL

__all__ = ["MonitoringService"]


class MonitoringService:

    def __init__(self):
        self.cores = psutil.cpu_count()

    def utilization(self, interval: float) -> Usage:
        """Возвращает список, усредненную загрузки каждого ядра.
        Номера ядер соответствуют порядку в списке.
        :param interval: Интервал времени
        :return:
        """
        usage: float | list[float] = psutil.cpu_percent(interval, percpu=True)
        data = Usage(
            cores=self.cores,
            usage=" ".join(map(str, usage)),
            at=time.time()
        )

        return data

    def monitor(self, connection: Connection, interval: int = 5):
        database = UsageDAL(connection)
        while True:
            database.insert(self.utilization(interval))

import sqlite3, time
from service import MonitoringService


class Database:
    database_name: str = ""
    table_name: str = "core_utilization_table"
    database_connect_1 = sqlite3.connect(database=database_name)
    database_connect_2 = sqlite3.connect(database=database_name)

    def __init__(self, name: str):
        self.database_name = name

    def create_table(self, ):
        cursor = self.database_connect_1.cursor()
        expression = f'''CREATE TABLE IF NOT EXISTS {self.table_name}(
                        timestamp REAL,
                        core_utilization TEXT)
                        '''
        cursor.execute(expression)
        self.database_connect_1.commit()

    def insert(self, core_utilization: float | list[float]):

        cursor = self.database_connect_1.cursor()
        expression = f"""INSERT INTO {self.table_name} (timestamp,core_utilization) VALUES ('{time.time()}', '{core_utilization}')
        """
        cursor.execute(expression)
        self.database_connect_1.commit()

    def select(self, interval: float, ):
        date_time_now = time.time()
        cursor = self.database_connect_2.cursor()
        expression = f"""SELECT * FROM {self.table_name} WHERE timestamp > ({date_time_now}-{interval})
                """
        cursor.execute(expression)
        return cursor.fetchall()

    def delete(self, border_1: float, border_2: float):
        cursor = self.database_connect_1.cursor()
        expression = f"""DELETE * FROM {self.table_name} WHERE (timestamp <={border_2} AND timestamp >= {border_1})
                """
        cursor.execute(expression)
        self.database_connect_1.commit()

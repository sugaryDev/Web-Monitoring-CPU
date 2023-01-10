from datetime import datetime
from sqlite3 import Connection

from models import Usage

__all__ = ["UsageDAL"]


class UsageDAL:

    def __init__(self, connection: Connection):
        self.connection = connection

    def initialize(self):
        statement = """
           CREATE TABLE IF NOT EXISTS usage (
               cores INTEGER, 
               usage TEXT, 
               at REAL
           );
           """
        cursor = self.connection.cursor()
        cursor.execute(statement)
        self.connection.commit()

    def insert(self, usage: Usage):
        statement = f"""
        INSERT INTO usage (cores, usage, at) VALUES (
            {usage.cores}, 
            '{usage.usage}', 
            {usage.at}
        );
        """
        cursor = self.connection.cursor()
        cursor.execute(statement)
        self.connection.commit()

    def select(self, interval: int) -> list[Usage]:
        delta = datetime.now().timestamp() - interval

        cursor = self.connection.cursor()
        statement = f"SELECT * FROM usage WHERE at > {delta}"
        cursor.execute(statement)

        data = cursor.fetchall()
        return [Usage(cores=cores, usage=usage, at=at) for cores, usage, at in data]

    def delete_all(self):
        cursor = self.connection.cursor()
        expression = """DELETE FROM usage"""
        cursor.execute(expression)
        self.connection.commit()
        self.connection.close()

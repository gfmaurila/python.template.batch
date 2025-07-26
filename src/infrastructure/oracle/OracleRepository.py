import cx_Oracle
from domain.entities.RegionEntity import RegionEntity
import os

class OracleRepository:
    def __init__(self):
        dsn = cx_Oracle.makedsn("localhost", 1521, service_name="xe")
        self.connection = cx_Oracle.connect(user="system", password="oracle", dsn=dsn)

    def GetRegions(self) -> list[RegionEntity]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT REGION_ID, REGION_NAME FROM HR.REGIONS")
        rows = cursor.fetchall()
        return [RegionEntity(RegionId=row[0], RegionName=row[1] or "") for row in rows]
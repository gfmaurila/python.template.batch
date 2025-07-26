from pymongo import MongoClient
from domain.entities.RegionEntity import RegionEntity
from core.Config import GetSettings

class MongoRepository:
    def __init__(self):
        settings = GetSettings()
        self.client = MongoClient(settings.MONGO_LOG_CONN)
        self.db = self.client[settings.MONGO_LOG_DB]
        self.collection = self.db[settings.MONGO_LOG_COLLECTION]

    def InsertRegions(self, regions: list[RegionEntity]):
        documents = [region.__dict__ for region in regions]
        self.collection.insert_many(documents)
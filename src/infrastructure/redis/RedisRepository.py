import redis
from domain.entities.RegionEntity import RegionEntity

class RedisRepository:
    def __init__(self):
        self.client = redis.Redis(host="localhost", port=6379, db=0, password="Poc2Minimal@Api")

    def InsertRegions(self, regions: list[RegionEntity]):
        for region in regions:
            key = f"region:{region.RegionId}"
            self.client.hset(key, mapping=region.__dict__)
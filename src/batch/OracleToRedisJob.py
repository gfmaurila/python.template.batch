from core.interfaces.IBatchJob import IBatchJob
from infrastructure.oracle.OracleRepository import OracleRepository
from infrastructure.redis.RedisRepository import RedisRepository

class OracleToRedisJob(IBatchJob):
    def Handle(self):
        oracle = OracleRepository()
        redis_repo = RedisRepository()
        regions = oracle.GetRegions()
        redis_repo.InsertRegions(regions)
        print(f"[OracleToRedisJob] Inseridos {len(regions)} registros no Redis")
from core.interfaces.IBatchJob import IBatchJob
from infrastructure.oracle.OracleRepository import OracleRepository
from infrastructure.mongo.MongoRepository import MongoRepository

class OracleToMongoJob(IBatchJob):
    def Handle(self):
        oracle = OracleRepository()
        mongo = MongoRepository()
        regions = oracle.GetRegions()
        mongo.InsertRegions(regions)
        print(f"[OracleToMongoJob] Inseridos {len(regions)} registros no MongoDB")
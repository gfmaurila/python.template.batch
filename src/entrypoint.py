import sys
from batch.OracleToMongoJob import OracleToMongoJob
from batch.OracleToRedisJob import OracleToRedisJob

def main():
    if len(sys.argv) < 2:
        print("Informe o job: mongo ou redis")
        return

    job_type = sys.argv[1].lower()

    if job_type == "mongo":
        OracleToMongoJob().Handle()
    elif job_type == "redis":
        OracleToRedisJob().Handle()
    else:
        print("Job inválido. Use: mongo ou redis")

if __name__ == "__main__":
    main()
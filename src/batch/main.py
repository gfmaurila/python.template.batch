from batch.OracleToMongoJob import OracleToMongoJob
from batch.OracleToRedisJob import OracleToRedisJob

if __name__ == "__main__":
    print("1. Oracle → MongoDB")
    print("2. Oracle → Redis")
    choice = input("Escolha o job a executar (1 ou 2): ").strip()

    if choice == "1":
        job = OracleToMongoJob()
    elif choice == "2":
        job = OracleToRedisJob()
    else:
        print("Opção inválida")
        exit(1)

    job.Handle()
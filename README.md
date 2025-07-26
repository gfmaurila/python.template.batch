

# 📦 Projeto Python Batch – Bulk Insert Oracle → MongoDB e Redis

## 📖 Visão Geral

Este projeto é um **Batch Job** escrito em Python, com base nos princípios de:

- ✅ DDD (Domain-Driven Design)
- ✅ CQRS (Command Query Responsibility Segregation)
- ✅ Padrão de nomenclatura e estrutura similar a projetos em C#
- ✅ Execução independente via linha de comando (ou cronjob/CI)
- ✅ Integração com Oracle, MongoDB e Redis

Seu objetivo inicial é executar a **carga de dados em lote (bulk insert)** de tabelas Oracle para:

- **MongoDB**: para persistência histórica
- **Redis**: para uso como cache rápido

---

## 🏗 Estrutura do Projeto

```bash
python.template.batch/
└── src/
    ├── batch/
    │   ├── OracleToMongoJob.py              # Job para gravar dados no MongoDB
    │   ├── OracleToRedisJob.py              # Job para gravar dados no Redis
    │   ├── main.py                          # Dispatcher de múltiplos jobs
    ├── application/
    │   └── ExampleJob/
    │       ├── commands/
    │       │   └── ExecuteExampleJobCommand.py
    │       └── services/
    │           └── ExampleJobService.py
    ├── core/
    │   ├── interfaces/
    │   │   └── IBatchJob.py                 # Interface padrão para jobs
    │   └── services/
    │       └── LoggerService.py             # Logger customizado
    ├── domain/
    │   └── entities/
    │       └── EmployeeEntity.py
    ├── infrastructure/
    │   ├── oracle/OracleRepository.py       # Leitura de dados Oracle
    │   ├── mongo/MongoRepository.py         # Escrita no MongoDB
    │   └── redis/RedisRepository.py         # Escrita no Redis
└── README.md
```

---

## 🚀 Como Executar o Projeto

### 🔧 Localmente com Python

```bash
pip install -r requirements.txt

# Executa job para MongoDB
python src/batch/OracleToMongoJob.py

# Executa job para Redis
python src/batch/OracleToRedisJob.py

# Ou usa o dispatcher principal
python src/batch/main.py
```

---

## 🐳 Docker Oracle XE (para testes)

Adicione ao seu `docker-compose.yml`:

```yaml
oracle-db:
  image: oracleinanutshell/oracle-xe-11g
  container_name: oracle_db
  ports:
    - "49161:1521"
    - "8080:8080"
  environment:
    - ORACLE_ALLOW_REMOTE=true
    - ORACLE_DISABLE_ASYNCH_IO=true
  restart: always
  networks:
    - app-backend
```

---

## 🔌 Tecnologias

- Python 3.11+
- Oracle XE (via Docker)
- MongoDB
- Redis
- `cx_Oracle`, `pymongo`, `redis-py`, `logging`, `dotenv`

---

## 🧠 Padrões e Convenções

- Jobs implementam a interface `IBatchJob` com método `Handle()`
- Comandos seguem o padrão `CommandHandler`
- Estrutura e nomes idênticos ao modelo usado em projetos C#
- Domínio separado por entidades e serviços de aplicação

---

## 📫 Como me encontrar
- [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCjy19AugQHIhyE0Nv558jcQ)
- [![Linkedin Badge](https://img.shields.io/badge/-Guilherme_Figueiras_Maurila-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/guilherme-maurila)](https://www.linkedin.com/in/guilherme-maurila)
- [![Gmail Badge](https://img.shields.io/badge/-gfmaurila@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:gfmaurila@gmail.com)](mailto:gfmaurila@gmail.com)
- 📧 Email: gfmaurila@gmail.com

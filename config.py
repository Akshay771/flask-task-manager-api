import os

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")
DB_NAME = os.getenv("DB_NAME", "tasksdb")
DB_HOST = os.getenv("DB_HOST", "pgdb")

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
# SQLALCHEMY_DATABASE_URI = "sqlite:///tasks.db"

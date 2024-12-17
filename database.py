from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:2123@localhost:5432/postgres"

# Создаем подключение
try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    connection = engine.connect()
    print("✅ Подключение к базе данных успешно!")
    connection.close()
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

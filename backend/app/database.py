import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Читаємо DATABASE_URL із змінних оточення, або повертаємо дефолт
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://mailgather_user:DMINDEui28u834fu9UMIEI93fj934if@db:5432/mailgather_db",
)

# Створюємо SQLAlchemy Engine
engine = create_engine(DATABASE_URL)

# Сеанс для роботи з БД (синхронний)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовий клас для моделей
Base = declarative_base()

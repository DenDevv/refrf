from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

# При першому запуску створюємо всі таблиці
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Додаємо CORS (щоб фронтенд міг робити запити з http://localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost"
    ],  # можна конкретизувати до ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/subscribe", status_code=201)
def subscribe(subscriber: schemas.SubscriberCreate, db: Session = Depends(get_db)):
    # Перевіряємо, чи такий email уже в базі
    existing = (
        db.query(models.Subscriber)
        .filter(models.Subscriber.email == subscriber.email)
        .first()
    )

    if existing:
        raise HTTPException(status_code=400, detail="Email already exists!")

    new_sub = models.Subscriber(email=subscriber.email)
    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)
    return {"id": new_sub.id, "email": new_sub.email}

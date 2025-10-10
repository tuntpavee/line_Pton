import os
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)  # postgres driver comes from .env
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class LineUser(Base):
    __tablename__ = "line_users"
    line_user_id = Column(String, primary_key=True)
    display_name = Column(String)
    picture_url = Column(String)
    email = Column(String)
    updated_at = Column(DateTime)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/healthz")
def health():
    return {"ok": True}

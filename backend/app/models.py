# backend/app/models.py
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, JSON as SA_JSON


class Scenario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    inputs: dict = Field(sa_column=Column(SA_JSON))
    results: dict = Field(sa_column=Column(SA_JSON))
    created_at: datetime = Field(default_factory=datetime.utcnow)

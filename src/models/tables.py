from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
import datetime


class Session(SQLModel, table=True):
    uuid: UUID = Field(default_factory=uuid4(), primary_key=True, index=True)
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now(tz=datetime.UTC))
    
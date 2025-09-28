from datetime import datetime
from sqlite3 import complete_statement
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from database_settings import engine


class Base(DeclarativeBase):
    pass


class Cats(Base):
    __tablename__ = "cats"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    experience: Mapped[int] = mapped_column(nullable=False)
    breed: Mapped[str] = mapped_column(nullable=False)
    salary: Mapped[float] = mapped_column(nullable=False)

    mission: Mapped["Missions"] = relationship(back_populates="cat", uselist=False)

class Missions(Base):
    __tablename__ = "missions"

    id: Mapped[int] = mapped_column(primary_key=True)
    cat_id: Mapped[int] = mapped_column(ForeignKey("cats.id"), nullable=True, unique=True)
    complete: Mapped[bool] = mapped_column(nullable=False, default=False)


    targets: Mapped[list["Targets"]] = relationship(
        "Targets",
        back_populates="mission",
        cascade="all, delete-orphan"
    )
    cat: Mapped["Cats"] = relationship(back_populates="mission")

    

class Targets(Base):
    __tablename__ = "targets"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    country: Mapped[str] = mapped_column(nullable=False)
    notes: Mapped[str] = mapped_column(default="")
    complete: Mapped[bool] = mapped_column(nullable=False, default=False)
    mission_id: Mapped[int] = mapped_column(ForeignKey('missions.id'))

    mission: Mapped["Missions"] = relationship(back_populates="targets")

async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
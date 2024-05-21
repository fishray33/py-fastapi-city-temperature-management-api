from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from database import Base


class DBCity(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(225), nullable=False, unique=True)
    additional_info = Column(String(1023))

    temperatures = relationship(
        "DBTemperature",
        back_populates="city",
        cascade='delete',
        passive_deletes=True
    )


class DBTemperature(Base):
    __tablename__ = "temperatures"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime, nullable=False)
    temperature = Column(Float, nullable=False)
    city_id = Column(
        Integer,
        ForeignKey("cities.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    city = relationship("DBCity", back_populates="temperatures")

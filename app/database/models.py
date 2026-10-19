
from sqlalchemy import Column, Integer, Float
from app.database.session import Base


class HousePredictionRecord(Base):
    __tablename__ = "house_predictions"

    id = Column(Integer, primary_key=True, index=True)

    MedInc = Column(Float, nullable=False)
    HouseAge = Column(Float, nullable=False)
    AveRooms = Column(Float, nullable=False)
    AveBedrms = Column(Float, nullable=False)
    Population = Column(Float, nullable=False)
    AveOccup = Column(Float, nullable=False)
    Latitude = Column(Float, nullable=False)
    Longitude = Column(Float, nullable=False)

    predicted_value = Column(Float, nullable=False)
    estimated_price_usd = Column(Float, nullable=False)

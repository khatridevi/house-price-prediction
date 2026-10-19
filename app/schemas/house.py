from pydantic import BaseModel


class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


class HousePrediction(BaseModel):
    predicted_value: float
    estimated_price_usd: float

if __name__ == "__main__":
    house = HouseFeatures(
        MedInc=5.0,
        HouseAge=20.0,
        AveRooms=6.0,
        AveBedrms=1.0,
        Population=1000.0,
        AveOccup=3.0,
        Latitude=34.05,
        Longitude=-118.25
    )

    print("Schema created successfully!")
    print(house)
    print(house.model_dump())
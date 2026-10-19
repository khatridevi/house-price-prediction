from fastapi import APIRouter

from app.schemas.house import HouseFeatures, HousePrediction
from app.services.prediction_service import predict_house_price

router = APIRouter(
    prefix="/predict",
    tags=["House Price Prediction"]
)


@router.post("/", response_model=HousePrediction)
def predict(data: HouseFeatures):
    return predict_house_price(data)


if __name__ == "__main__":
    print("Prediction router is configured.")
    print("Endpoint: POST /predict/")
    
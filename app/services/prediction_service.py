from pathlib import Path

import joblib
import pandas as pd
from sqlalchemy import text
from app.schemas.house import HouseFeatures
from app.database.session import SessionLocal
from app.database.models import HousePredictionRecord
# Find the trained model file
BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"
# Load the trained model
model = joblib.load(MODEL_PATH)
def predict_house_price(data: HouseFeatures) -> dict:
    # Prepare input features
    input_data = pd.DataFrame([data.model_dump()])
    # Predict the house value
    prediction = float(model.predict(input_data)[0])
    # Convert the value into US dollars
    result = {
        "predicted_value": round(prediction, 3),
        "estimated_price_usd": round(prediction * 100000, 2)
    }
    # Open a database session
    db = SessionLocal()
    try:
        # Check the active database connection
        info = db.execute(
            text(
                "SELECT @@SERVERNAME AS server_name, "
                "DB_NAME() AS database_name"
            )
        ).mappings().one()
        print("Database connection:", dict(info))
        # Create a database record
        record = HousePredictionRecord(
            **data.model_dump(),
            predicted_value=result["predicted_value"],
            estimated_price_usd=result["estimated_price_usd"]
        )
        # Save the record
        db.add(record)
        db.commit()
        db.refresh(record)
        print("Record saved successfully. ID:", record.id)
    except Exception as error:
        db.rollback()
        print("DATABASE SAVE FAILED:", repr(error))
        raise
    finally:
        db.close()
    return result
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
    result = predict_house_price(house)
    print("Prediction successful!")
    print(result)
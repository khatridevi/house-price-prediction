
from app.database.session import engine, Base
from app.database.models import HousePredictionRecord

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")

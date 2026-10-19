# House Price Prediction API 
# 🏠 House Price Prediction API

A full-stack Machine Learning application built with **FastAPI** for the backend API service and **Streamlit** for an interactive web frontend interface. The application predicts house prices based on various input parameters using a trained machine learning model.

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Python, Uvicorn, SQLAlchemy
* **Frontend:** Streamlit
* **Machine Learning:** Scikit-learn, Joblib
* **Data Processing:** Pandas, NumPy

---

## 📁 Project Structure

```text
house-price-prediction-api/
│
├── app/
│   ├── database/          # Database configuration & session setup
│   ├── models/            # SQLAlchemy database models
│   ├── routers/           # FastAPI routes & endpoints
│   ├── schemas/           # Pydantic models for request/response validation
│   ├── services/          # Business logic & ML model inference
│   └── main.py            # FastAPI entry point
│
├── frontend/
│   ├── app.py             # Streamlit user interface application
│   └── predictions_history.csv  # Saved predictions log
│
└── requirements.txt       # Project dependencies

🚀 Getting Started
Follow these steps to run the project locally on your machine.

1. Clone the Repository
Bash
git clone [https://github.com/khatridevi/house-price-prediction.git](https://github.com/khatridevi/house-price-prediction.git)
cd house-price-prediction
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Run the Backend (FastAPI)
Start the FastAPI server:

Bash
uvicorn app.main:app --reload
The backend API will be available at: http://127.0.0.1:8000

Swagger UI documentation: http://127.0.0.1:8000/docs

4. Run the Frontend (Streamlit)
In a new terminal window, start the Streamlit web application:

Bash
streamlit run frontend/app.py
The application will open automatically in your browser at http://localhost:8501.

📝 Features
Interactive Streamlit dashboard for house price prediction.

RESTful API backend using FastAPI.

Logs prediction history for record-keeping.


---

### Steps after pasting:
1. Save the file in VS Code (`Ctrl + S`).
2. Open your terminal in `C:\Dotcom\my-first-api\house-price-prediction-api`.
3. Run these 3 commands:
   ```bash
   git add README.md
   git commit -m "Add README file"
   git push origin main
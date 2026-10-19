import requests
import streamlit as st
import pandas as pd
import os

API_URL = "http://127.0.0.1:8000/predict/"
CSV_FILE = "predictions_history.csv"

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.title("House Price Prediction")
st.write("Enter the house details to estimate its value.")

with st.form("house_prediction_form"):
    st.subheader("House Features")

    med_inc = st.number_input(
        "Median Income (in tens of thousands of dollars)",
        min_value=0.0,
        value=5.0,
        step=0.1
    )

    house_age = st.number_input(
        "House Age (years)",
        min_value=0.0,
        value=20.0,
        step=1.0
    )

    ave_rooms = st.number_input(
        "Average Rooms",
        min_value=0.0,
        value=6.0,
        step=0.1
    )

    ave_bedrms = st.number_input(
        "Average Bedrooms",
        min_value=0.0,
        value=1.0,
        step=0.1
    )

    population = st.number_input(
        "Block Population",
        min_value=0.0,
        value=1000.0,
        step=10.0
    )

    ave_occup = st.number_input(
        "Average Occupancy",
        min_value=0.0,
        value=3.0,
        step=0.1
    )

    latitude = st.number_input(
        "Latitude",
        min_value=-90.0,
        max_value=90.0,
        value=34.05,
        step=0.01
    )

    longitude = st.number_input(
        "Longitude",
        min_value=-180.0,
        max_value=180.0,
        value=-118.25,
        step=0.01
    )

    submitted = st.form_submit_button("Predict House Price")

if submitted:
    payload = {
        "MedInc": med_inc,
        "HouseAge": house_age,
        "AveRooms": ave_rooms,
        "AveBedrms": ave_bedrms,
        "Population": population,
        "AveOccup": ave_occup,
        "Latitude": latitude,
        "Longitude": longitude
    }

    try:
        response = requests.post(
            API_URL,
            json=payload,
            timeout=30
        )

        response.raise_for_status()
        result = response.json()

        st.success("Prediction completed successfully!")

        estimated_price = result['estimated_price_usd']

        st.metric(
            "Estimated House Value",
            f"${estimated_price:,.2f}"
        )

        st.caption(
            f"Model prediction: {result['predicted_value']:.3f} "
            "in units of $100,000."
        )

        # --- NEW CODE: Save Prediction to CSV History ---
        new_record = pd.DataFrame([{
            "Median Income": med_inc,
            "House Age": house_age,
            "Population": population,
            "Estimated Price ($)": f"${estimated_price:,.2f}"
        }])

        if os.path.exists(CSV_FILE):
            new_record.to_csv(CSV_FILE, mode='a', header=False, index=False)
        else:
            new_record.to_csv(CSV_FILE, mode='w', header=True, index=False)

    except requests.exceptions.ConnectionError:
        st.error(
            "Cannot connect to the FastAPI server. "
            "Start the backend using Uvicorn and try again."
        )

    except requests.exceptions.RequestException as error:
        st.error(f"API request failed: {error}")

# --- DISPLAY PREDICTIONS HISTORY LIST ---
st.markdown("---")
st.subheader("📜 Previous Predictions History")

if os.path.exists(CSV_FILE):
    history_df = pd.read_csv(CSV_FILE)
    st.dataframe(history_df, use_container_width=True)
    st.write(f"**Total Predictions Made:** {len(history_df)}")
else:
    st.info("No predictions made yet.")
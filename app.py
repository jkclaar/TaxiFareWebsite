import streamlit as st
import requests
import datetime

"""
# TaxiFareModel front
"""

st.markdown(
    """
yess indeed
"""
)

"""
## Do some inputs guy

"""

d = st.date_input("When are you travelling?", datetime.date.today())
t = st.time_input("What time?", datetime.datetime.now())

pickup_long = st.number_input("pickup longitude")
pickup_lat = st.number_input("pickup latitude")
dropoff_long = st.number_input("dropoff longitude")
dropoff_lat = st.number_input("dropoff latitude")

passenger_count = st.slider("Passenger count", 1, 6, 1)

url = "https://taxifare.lewagon.ai/predict"

params = {
    "pickup_datetime": f"{d} {t}",
    "pickup_longitude": pickup_long,
    "pickup_latitude": pickup_lat,
    "dropoff_longitude": dropoff_long,
    "dropoff_latitude": dropoff_lat,
    "passenger_count": passenger_count,
}

response = requests.get(url, params=params).json()
prediction = response["prediction"]

if st.button("click me"):
    # print is visible in the server output, not in the page
    print("button clicked!")
    st.success(f"the fare will be {prediction} 🎉")

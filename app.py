import streamlit as st
import datetime
import requests



'''
# TaxiFareModel
'''




st.markdown(''' ### Fill the date and time of pickup''')

date = st.date_input("Pickup date", datetime.date(2014, 7, 6))
time = st.time_input("Pickup time")

pickup_datetime = datetime.datetime.combine(date, time).strftime("%Y-%m-%d %H:%M:%S")



st.markdown('''### Fill the pickup coordinates :''')

pickup_longitude = st.number_input('Pickup Longitude [-74.3 to -73.7] :')
pickup_latitude = st.number_input('Pickup Latitude [40.5 to 40.9] :')

st.write('The coordinates are ', pickup_longitude, pickup_latitude)

st.markdown('''### Fill the dropoff coordinates :''')

dropoff_longitude = st.number_input('Dropoff Longitude [-74.3 to -73.7] :')
dropoff_latitude = st.number_input('Dropoff Latitude [40.5 to 40.9] :')
st.write('The coordinates are ', dropoff_longitude, dropoff_latitude)

st.markdown('''### Fill the passenger count :''')

passenger_count = st.number_input('Number of passenger [0 to 8] :')
st.write('The number of passenger is ', passenger_count)


url = 'https://taxifare-1042182811091.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

data = {
        "pickup_datetime" : pickup_datetime,
        "pickup_longitude" : pickup_longitude,
        "pickup_latitude" : pickup_latitude,
        "dropoff_longitude" : dropoff_longitude,
        "dropoff_latitude" : dropoff_latitude,
        "passenger_count" : passenger_count,
    }
st.markdown('## Fare prediction')
if st.button("Amount prediction"):
    try:
    # Sending POST request
        response = requests.get(url, params=data)
        #st.write(response.url)
        st.success("Request sent successfully!")
        st.write("Response Status Code:", response.status_code)
       # st.write(response.text)
        st.write("Fare amount :",response.json()['fare']) # Display JSON response
    except Exception as e:
       st.error(f"An error occurred: {e}")

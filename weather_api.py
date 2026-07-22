import streamlit as st
import matplotlib.pyplot as plt
import requests

st.set_page_config(
    page_title="Weather App",
    page_icon="🌤",
    layout='wide'
)

st.title("🌤 Weather App")

api_key = "bfa01def98de401a1710b42a056dd295"

city = st.text_input("Enter City", "Ahmedabad")

if st.button("Get Weather"):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:

        st.subheader(data["name"])

        st.write("Temperature:", data["main"]["temp"], "°C")
        st.write("Feels Like:", data["main"]["feels_like"], "°C")
        st.write("Humidity:", data["main"]["humidity"], "%")
        st.write("Wind Speed:", data["wind"]["speed"], "m/s")
        st.write("Visibility:", data["visibility"]/1000, "km")
      
        st.write("Condition:", data["weather"][0]["description"])

        weather = {
            "Temp": data["main"]["temp"],
            "Feels Like": data["main"]["feels_like"],
            "Min Temp": data["main"]["temp_min"],
            "Max Temp": data["main"]["temp_max"],
            "Humidity": data["main"]["humidity"]
        }
        fig, ax = plt.subplots(figsize=(5, 3))

        ax.bar(weather.keys(), weather.values())

        ax.set_title(f"Weather in {city}")
        ax.set_ylabel("Value")

        plt.xticks(rotation=30)

        st.pyplot(fig, use_container_width=False)

    else:
        st.error("City not found")

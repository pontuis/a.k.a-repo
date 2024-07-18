import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import requests
from datetime import datetime
import speech_recognition as sr
import threading
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 125)


def fetch_weather(city):
    api_key = "49e5d4fb8e31c6f57ee2acc6113d3488"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    if not city:
        display_error("Please enter a valid city name.")
        return

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200 or "main" not in data:
            display_error(f"Error: {data.get('message', 'City not found or API error')}")
            return

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        icon_code = data["weather"][0]["icon"]
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]

        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        forecast_response = requests.get(forecast_url, timeout=10)
        forecast_data = forecast_response.json()
        forecast = [
            {
                "time": datetime.fromtimestamp(forecast_data["list"][i]["dt"]).strftime('%H:%M'),
                "temp": forecast_data["list"][i]["main"]["temp"],
                "condition": forecast_data["list"][i]["weather"][0]["description"],
                "icon": forecast_data["list"][i]["weather"][0]["icon"]
            } for i in range(0, 24, 8)
        ]

        update_ui(temp, condition, icon_code, wind_speed, humidity, forecast, city)
    except requests.RequestException:
        display_error("Network error. Please check your internet connection.")


def update_ui(temp, condition, icon_code, wind_speed, humidity, forecast, city):
    temperature_label.configure(text=f"{temp}°C")
    condition_label.configure(text=condition.capitalize())
    wind_label.configure(text=f"Wind: {wind_speed} m/s")
    humidity_label.configure(text=f"Humidity: {humidity}%")

    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    icon_img = Image.open(requests.get(icon_url, stream=True).raw)
    icon_img = icon_img.resize((100, 100), Image.LANCZOS)
    weather_icon = ImageTk.PhotoImage(icon_img)
    weather_icon_label.configure(image=weather_icon)
    weather_icon_label.image = weather_icon

    for i, fc in enumerate(forecast):
        forecast_labels[i].configure(text=f"{fc['time']}: {fc['temp']}°C, {fc['condition']}")
        icon_url = f"http://openweathermap.org/img/wn/{fc['icon']}@2x.png"
        icon_img = Image.open(requests.get(icon_url, stream=True).raw)
        icon_img = icon_img.resize((50, 50), Image.LANCZOS)
        forecast_icons[i].configure(image=ImageTk.PhotoImage(icon_img))
        forecast_icons[i].image = ImageTk.PhotoImage(icon_img)

    speak_weather_result(city, temp, condition, wind_speed, humidity, forecast)


def display_error(message):
    error_label.configure(text=message)
    temperature_label.configure(text="N/A")
    condition_label.configure(text="N/A")
    wind_label.configure(text="Wind: N/A")
    humidity_label.configure(text="Humidity: N/A")
    weather_icon_label.configure(image="")
    for i in range(3):
        forecast_labels[i].configure(text="")
        forecast_icons[i].configure(image="")

    engine.say("City does not exist, please say the exact city you want me to search")
    engine.runAndWait()


# The rest of your code remains the same

def update_weather():
    city = city_var.get()
    if city:
        fetch_weather(city)
    app.after(600000, update_weather)


app = ctk.CTk()
app.title("Weather Application")
app.geometry("1024x768")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

main_frame = ctk.CTkFrame(app, corner_radius=15)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

weather_frame = ctk.CTkFrame(main_frame, corner_radius=15)
weather_frame.grid(row=0, column=0, rowspan=2, padx=20, pady=20, sticky="nsew")

background_label = ctk.CTkLabel(weather_frame, text="")
background_label.pack(pady=10)

input_frame = ctk.CTkFrame(main_frame, corner_radius=15)
input_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

city_entry = ctk.CTkEntry(input_frame, placeholder_text="Enter city name", width=200, height=30, font=("Helvetica", 14))
city_entry.pack(pady=10)
add_city_button = ctk.CTkButton(input_frame, text="Add City", command=add_city, font=("Helvetica", 14))
add_city_button.pack(pady=5)

city_var = ctk.StringVar(value="your_city")  # Set default city
city_options = ["your_city"]  # Default city
city_menu = ctk.CTkOptionMenu(input_frame, variable=city_var, values=city_options, width=200, height=30,
                              font=("Helvetica", 14))
city_menu.pack(pady=5)

temperature_label = ctk.CTkLabel(weather_frame, text="N/A", font=("Helvetica", 36))
temperature_label.pack(pady=10)
condition_label = ctk.CTkLabel(weather_frame, text="N/A", font=("Helvetica", 18))
condition_label.pack(pady=10)
wind_label = ctk.CTkLabel(weather_frame, text="Wind: N/A", font=("Helvetica", 16))
wind_label.pack(pady=5)
humidity_label = ctk.CTkLabel(weather_frame, text="Humidity: N/A", font=("Helvetica", 16))
humidity_label.pack(pady=5)

weather_icon_label = ctk.CTkLabel(weather_frame, text="")
weather_icon_label.pack(pady=10)

forecast_labels = []
forecast_icons = []
for _ in range(3):
    icon_label = ctk.CTkLabel(weather_frame, text="")
    icon_label.pack(side="left", padx=5)
    forecast_icons.append(icon_label)
    label = ctk.CTkLabel(weather_frame, text="", font=("Helvetica", 14))
    label.pack(side="left", padx=5)
    forecast_labels.append(label)

time_label = ctk.CTkLabel(main_frame, text="", font=("Helvetica", 24))
time_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
date_label = ctk.CTkLabel(main_frame, text="", font=("Helvetica", 24))
date_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")

voice_command_button = ctk.CTkButton(main_frame, text="Voice Command", command=start_voice_command,
                                     font=("Helvetica", 14))
voice_command_button.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

voice_output_label = ctk.CTkLabel(main_frame, text="", font=("Helvetica", 14))
voice_output_label.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

error_label = ctk.CTkLabel(main_frame, text="", font=("Helvetica", 14), text_color="red")
error_label.grid(row=4, column=0, columnspan=2, pady=10)

theme_label = ctk.CTkLabel(main_frame, text="Select Theme", font=("Helvetica", 16))
theme_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")
theme_menu = ctk.CTkOptionMenu(main_frame, values=["dark", "light"], command=change_theme, width=200, height=30,
                               font=("Helvetica", 14))
theme_menu.grid(row=5, column=0, padx=20, pady=10, sticky="e")

text_size_slider = ctk.CTkSlider(main_frame, from_=12, to=36, number_of_steps=24,
                                 command=lambda size: change_text_size(int(size)))
text_size_slider.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
text_size_label = ctk.CTkLabel(main_frame, text="Text Size", font=("Helvetica", 16))
text_size_label.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky="n")

update_time_date()
fetch_weather(city_options[0])

app.after(600000, update_weather)

app.mainloop()

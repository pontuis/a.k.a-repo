import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox, scrolledtext
import matplotlib.pyplot as plt
import mysql.connector
import requests


class WeatherApp:
    def _init_(self, root, api_key, app_config):

        self.root = root
        self.api_key = api_key
        self.app_config = app_config

        self.root.title("Weather App")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        # Header
        self.header = tk.Label(root, text="Weather App", font=("Arial", 24), bg='#f0f0f0')
        self.header.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        # City entry and button
        self.city_label = tk.Label(root, text="Enter City:", font=("Arial", 18), bg='#f0f0f0')
        self.city_label.grid(row=1, column=0, padx=20, pady=20)
        self.city_entry = tk.Entry(root, width=30, font=("Arial", 18))
        self.city_entry.grid(row=1, column=1, padx=20, pady=20)
        self.get_weather_button = tk.Button(root, text="Get Current Weather", font=("Arial", 18), command=self.fetch_and_display_current_weather)
        self.get_weather_button.grid(row=1, column=2, padx=20, pady=20)

        # Current weather display
        self.current_weather_label = scrolledtext.ScrolledText(root, width=60, height=10, font=("Arial", 18), wrap=tk.WORD)
        self.current_weather_label.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

        # Weather icons
        self.weather_icon = tk.Label(root, text="", font=("Arial", 24), bg='#f0f0f0')
        self.weather_icon.grid(row=3, column=0, padx=20, pady=20)

        # Alert setup
        self.alert_threshold_label = tk.Label(root, text="Set Alert Temperature Threshold:", font=("Arial", 18), bg='#f0f0f0')
        self.alert_threshold_label.grid(row=4, column=0, padx=20, pady=20)
        self.alert_threshold_entry = tk.Entry(root, width=30, font=("Arial", 18))
        self.alert_threshold_entry.grid(row=4, column=1, padx=20, pady=20)
        self.alert_message_label = tk.Label(root, text="Set Alert Message:", font=("Arial", 18), bg='#f0f0f0')
        self.alert_message_label.grid(row=5, column=0, padx=20, pady=20)
        self.alert_message_entry = tk.Entry(root, width=30, font=("Arial", 18))
        self.alert_message_entry.grid(row=5, column=1, padx=20, pady=20)
        self.set_alert_button = tk.Button(root, text="Set Alert", font=("Arial", 18), command=self.set_alert)
        self.set_alert_button.grid(row=5, column=2, padx=20, pady=20)

        # Historical data plot
        self.plot_button = tk.Button(root, text="Plot Historical Data", font=("Arial", 18), command=self.plot_historical_data)
        self.plot_button.grid(row=6, column=0, columnspan=3, padx=20, pady=20)

    def fetch_and_display_current_weather(self):
        # Fetch weather data and display it
        pass

    def fetch_historical_data(self):
        # Fetch historical weather data from database
        pass

    def save_weather_data_to_app(self):
        # Save weather data to database
        pass

    def plot_historical_data(self):
        # Plot historical weather data
        pass

    def set_alert(self):
        # Set alert threshold and message
        pass

    def check_alerts(self):
        # Check if current temperature exceeds alert threshold
        pass

if __name__ == "_main_":
    app_config = {
        "host": "localhost",
        "user": "root",
        "password": "igetbacking24",
        "database": "weather_app"
    }
    api_key = "b8c4038152a8f408402562a3328aef1a"
    root = tk.Tk()
    app = WeatherApp(root, api_key, app_config)
    root.mainloop()

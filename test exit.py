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

        # UI setup
        self.root.title("Weather App")
        self.root.geometry("800x600")
        self.root.configure(bg='sky blue')

        # City entry and button
        self.city_label = tk.Label(root, text="Enter City:")
        self.city_label.grid(row=0, column=0, padx=20, pady=20)
        self.city_entry = tk.Entry(root, width=30)
        self.city_entry.grid(row=0, column=1, padx=20, pady=20)
        self.get_weather_button = tk.Button(root, text="Get Current Weather", command=self.fetch_and_display_current_weather)
        self.get_weather_button.grid(row=0, column=2, padx=20, pady=20)

        # Current weather display
        self.current_weather_label = scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD)
        self.current_weather_label.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

        # Alert setup
        self.alert_threshold_label = tk.Label(root, text="Set Alert Temperature Threshold:")
        self.alert_threshold_label.grid(row=2, column=0, padx=20, pady=20)
        self.alert_threshold_entry = tk.Entry(root, width=30)
        self.alert_threshold_entry.grid(row=2, column=1, padx=20, pady=20)
        self.alert_message_label = tk.Label(root, text="Set Alert Message:")
        self.alert_message_label.grid(row=3, column=0, padx=20, pady=20)
        self.alert_message_entry = tk.Entry(root, width=30)
        self.alert_message_entry.grid(row=3, column=1, padx=20, pady=20)
        self.set_alert_button = tk.Button(root, text="Set Alert", command=self.set_alert)
        self.set_alert_button.grid(row=3, column=2, padx=20, pady=20)


if __name__ == "__main__":
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
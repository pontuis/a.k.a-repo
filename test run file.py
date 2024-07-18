import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox, scrolledtext

import matplotlib.pyplot as plt
import mysql.connector
import requests

class WeatherApp:
    def __init__(self, root, api_key, app_config):
        self.api_key = api_key
        self.app_config = app_config
        self.root = root
        self.root.title("Weather forecast")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        self.header_frame = tk.Frame(self.root, bg='#333', height=50)
        self.header_frame.pack(fill='x')

        self.header_label = tk.Label(self.header_frame, text="Weather Forecast", font=("Arial", 20), fg='white', bg='#333')
        self.header_label.pack(pady=10)

        self.search_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.search_frame.pack(fill='x', padx=20, pady=20)

        self.city_label = tk.Label(self.search_frame, text="Enter City:", font=("Arial", 14), fg='#333')
        self.city_label.pack(side='left', padx=10)

        self.city_entry = tk.Entry(self.search_frame, width=30, font=("Arial", 14), fg='#333')
        self.city_entry.pack(side='left', padx=10)

        self.get_weather_button = tk.Button(self.search_frame, text="Get Weather", font=("Arial", 14), fg='white', bg='#337ab7', command=self.fetch_and_display_current_weather)
        self.get_weather_button.pack(side='left', padx=10)

        self.current_weather_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.current_weather_frame.pack(fill='both', expand=True, padx=20, pady=20)

        self.current_weather_label = tk.Label(self.current_weather_frame, text="", font=("Arial", 18), fg='#333', wraplength=600)
        self.current_weather_label.pack(pady=20)

        self.alert_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.alert_frame.pack(fill='x', padx=20, pady=20)

        self.alert_threshold_label = tk.Label(self.alert_frame, text="Set Alert Temperature Threshold:", font=("Arial", 14), fg='#333')
        self.alert_threshold_label.pack(side='left', padx=10)

        self.alert_threshold_entry = tk.Entry(self.alert_frame, width=20, font=("Arial", 14), fg='#333')
        self.alert_threshold_entry.pack(side='left', padx=10)

        self.alert_message_label = tk.Label(self.alert_frame, text="Set Alert Message:", font=("Arial", 14), fg='#333')
        self.alert_message_label.pack(side='left', padx=10)

        self.alert_message_entry = tk.Entry(self.alert_frame, width=20, font=("Arial", 14), fg='#333')
        self.alert_message_entry.pack(side='left', padx=10)

        self.set_alert_button = tk.Button(self.alert_frame, text="Set Alert", font=("Arial", 14), fg='white', bg='#337ab7', command=self.set_alert)
        self.set_alert_button.pack(side='left', padx=10)

        self.city_entry.insert(0, self.city_entry.get())
        self.fetch_and_display_current_weather()

    def fetch_and_display_current_weather(self):
        city = self.city_entry.get()
        if city:
            weather_data = self.fetch_weather(self.api_key, city)
            if weather_data.get('cod')!= 200:
                messagebox.showerror("Error", "City not found")
                return

            self.save_weather_data_to_app(city, weather_data)

            weather_info = f"City: {weather_data['name']}\n"
            weather_info += f"Temperature: {weather_data['main']['temp']}°C\n"
            weather_info += f"Conditions: {weather_data['weather'][0]['description']}"
            self.current_weather_label.config(text=weather_info)

            self.check_alerts(city, weather_data['main']['temp'])
            historical_data = self.fetch_historical_data(self.app_config, city=self.city_entry.get())
            self.plot_historical_data(historical_data)

    def fetch_weather(self, api_key, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        return response.json()

    # weather.py

    import argparse
    from configparser import ConfigParser

    BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

    # ...
    # weather.py

    # ...

PADDING = 20
REVERSE = "\033[;7m"
RESET = "\033[0m"

    # ...

def display_weather_info(weather_data, imperial=False):

        # ...

        city = weather_data["name"]
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]

        print(f"{REVERSE}{city:^{PADDING}}{RESET}", end="")
        print(
            f"\t{weather_description.capitalize():^{PADDING}}",
            end=" ",
        )
        print(f"({temperature}°{'F' if imperial else 'C'})")

def fetch_historical_data(self, db_config, city):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)

        query = "SELECT Temperature, Date FROM"

        query = "SELECT Temperature, Date FROM Weather WHERE City = %s AND Date BETWEEN %s AND %s ORDER BY Date"
        cursor.execute(query, (city, start_date, end_date))
        result = cursor.fetchall()

        cursor.close()
        conn.close()

        return result

def save_weather_data_to_app(self, city, weather_data):
        conn = mysql.connector.connect(**self.app_config)
        cursor = conn.cursor()

        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        date = datetime.now()

        query = "INSERT INTO Weather (City, Temperature, Description, Date) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (city, temperature, description, date))
        conn.commit()

        cursor.close()
        conn.close()

def plot_historical_data(self, data):
        dates = [x[1] for x in data]
        temps = [x[0] for x in data]

        plt.figure(figsize=(8, 5))
        plt.plot(dates, temps, marker='o', linestyle='-', color='b')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title(f"Historical Temperature in current city over the Past Week")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def set_alert(self):
        city = self.city_entry.get()
        try:
            threshold = float(self.alert_threshold_entry.get())
            message = self.alert_message_entry.get()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the threshold.")
            return

        conn = mysql.connector.connect(**self.app_config)
        cursor = conn.cursor()

        query = "INSERT INTO Alerts (City, TemperatureThreshold, AlertMessage) VALUES (%s, %s, %s)"
        cursor.execute(query, (city, threshold, message))
        conn.commit()

        cursor.close()
        conn.close()

        messagebox.showinfo("Success", "Alert set successfully!")

def check_alerts(self, city, current_temp):
        conn = mysql.connector.connect(**self.app_config)
        cursor = conn.cursor()

        query = "SELECT TemperatureThreshold, AlertMessage FROM Alerts WHERE City = %s"
        cursor.execute(query, (city,))
        alerts = cursor.fetchall()

        cursor.close()
        conn.close()

        for threshold, message in alerts:
            if current_temp >= threshold:
                messagebox.showwarning("Alert", message)
                break

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

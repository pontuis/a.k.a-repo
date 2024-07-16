
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
        self.root.title("Weather App")
        self.root.geometry("800x600")

        # self.root.iconbitmap('orange_eyes.icon')

        self.root.configure(bg='gray')

        self.city_label = tk.Label(root, text="Enter City:")
        self.city_label.grid(row=0, column=0, padx=20, pady=20)

        self.city_entry = tk.Entry(root, width=30)
        self.city_entry.grid(row=0, column=1, padx=20, pady=20)

        self.get_weather_button = tk.Button(root, text="Get Current Weather",
                                            command=self.fetch_and_display_current_weather)
        self.get_weather_button.grid(row=0, column=2, padx=20, pady=20)

        self.current_weather_label = scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD)
        self.current_weather_label.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

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

        self.city_entry.insert(0, self.city_entry.get())
        self.fetch_and_display_current_weather()

    def fetch_and_display_current_weather(self):
        city = self.city_entry.get()
        weather_data = self.fetch_weather(self.api_key, city)
        if weather_data.get('cod') != 200:
            messagebox.showerror("Error", "City not found")
            return

        self.save_weather_data_to_app(city, weather_data)

        weather_info = f"City: {weather_data['name']}\n"
        weather_info += f"Temperature: {weather_data['main']['temp']}°C\n"
        weather_info += f"Conditions: {weather_data['weather'][0]['description']}"
        self.current_weather_label.delete(1.0, tk.END)
        self.current_weather_label.insert(tk.END, weather_info)

        self.check_alerts(city, weather_data['main']['temp'])
        historical_data = self.fetch_historical_data(self.app_config, city=self.city_entry.get())
        self.plot_historical_data(historical_data)
    def fetch_weather(self, api_key, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        return response.json()

    def fetch_historical_data(self, db_config, city):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)

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
        plt.xlabel("Date")
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
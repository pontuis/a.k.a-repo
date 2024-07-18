import tkinter as tk
from typing import Tuple

import requests
import mysql.connector

# OpenWeatherMap API key
# API_KEY = "b8c4038152a8f408402562a3328aef1a"
#
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="igetbacking24",
#     database="weather_app"
# )
# cursor = db.cursor()
#

# cursor.executemany("""
#     CREATE TABLE IF NOT EXISTS current_weather (
#         id INT AUTO_INCREMENT,
#         city VARCHAR(50),
#         temperature FLOAT,
#         humidity FLOAT,
#         wind_speed FLOAT,
#         PRIMARY KEY (id)
#     );
# """)
#
# cursor.executemany("""
#     CREATE TABLE IF NOT EXISTS historical_weather (
#         id INT AUTO_INCREMENT,
#         city VARCHAR(50),
#         date DATE,
#         temperature FLOAT,
#         humidity FLOAT,
#         wind_speed FLOAT,
#         PRIMARY KEY (id)
#     );
# """)
#

# def fetch_current_weather(city):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
#     response = requests.get(url)
#     data = response.json()
#     return data
#

# def store_current_weather(city, temperature, humidity, wind_speed):
#     cursor.executemany("""
#         INSERT INTO current_weather (city, temperature, humidity, wind_speed)
#         VALUES (%s, %s, %s, %s);
#     """, (city, temperature, humidity, wind_speed))
#     db.commit()
#

# def fetch_historical_weather(city):
#     cursor.executemany("""
#         SELECT * FROM historical_weather
#         WHERE city = %s
#         ORDER BY date DESC;
#     """, (city,))
#     data = cursor.fetchall()
#     return data
#

# def plot_historical_weather(city):
#     data = fetch_historical_weather(city)
#     temperatures = [row[3] for row in data]
#     dates = [row[2] for row in data]
#
#     fig = "Figure"(figsize=(4, 3), dpi=100)
#     ax = fig.add_subplot(111)
#     ax.plot(dates, temperatures)
#     ax.set_title("Temperature over Time")
#     ax.set_xlabel("Date")
#     ax.set_ylabel("Temperature (°C)")
#
#     canvas = FigureCanvasTkAgg(fig, master=window)
#     canvas.draw()
#     canvas.get_tk_widget().pack()
#

# window = tk.Tk()
# window.title("Desktop Weather App")
#

# city_label = tk.Label(window, text="Enter city:")
# city_label.pack()
# city_entry = tk.Entry(window)
# city_entry.pack()
#

# def fetch_weather():
#     city = city_entry.get()
#     data = fetch_current_weather(city)
#     temperature = data["main"]["temp"]
#     humidity = data["main"]["humidity"]
#     wind_speed = data["wind"]["speed"]
#     store_current_weather(city, temperature, humidity, wind_speed)
#     plot_historical_weather(city)
#
# fetch_button = tk.Button(window, text="Fetch Weather", command=fetch_weather)
# fetch_button.pack()
#

# menu_bar = tk.Menu(window)
# file_menu = tk.Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Open")
# file_menu.add_command(label="Save")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=window.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)
# window.config(menu=menu_bar)

# window.mainloop



# import mysql.connector
#
#
# mydb = mysql.connector.connect(
#      host="localhost",
#      user="root",
#      password="igetbacking24",
#
# cursor = mydb.cursor()
# cursor.execute("DROP TABLE weather_apptb")
# for db in cursor:
#     print(cursor)
#


import mysql.connector

# Establish a connection to the database
cnx = mysql.connector.connect(
    user='root',
    password='igetbacking24',
    host='localhost',
    database='weather_app'
)

# Create a cursor object to execute queries
cursor = cnx.cursor()

# Create the weather_data table
query = """
    CREATE TABLE weather (
        id INT AUTO_INCREMENT PRIMARY KEY,
        city VARCHAR(50) NOT NULL,
        temperature FLOAT NOT NULL,
        description VARCHAR(100) NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        alert_temperature FLOAT,
        alert_description VARCHAR(100),
        alert_humidity varchar(100)
    )
"""
cursor.execute(query)

# Create the weather_alerts table
query = """
    CREATE TABLE alerts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        city VARCHAR(50) NOT NULL,
        alert_temperaturethreshold FLOAT NOT NULL,
        alert_description VARCHAR(100) NOT NULL,
         alert_humidity varchar(100)
    )
"""
cursor.execute(query)

# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
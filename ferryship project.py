# import tkinter as tk
# import requests
# import mysql.connector
# import matplotlib.pyplot as plt
#
#
# root = tk.Tk()
# root.title("Desktop Weather App")
#
# API_KEY = "b8c4038152a8f408402562a3328aef1a"
#
#
# class City:
#     pass
#
# base_url = f"(https(://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY})"
#
#
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="igetbacking24",
#     database="weather_app"
# )
#
#
# def plot_historical_trends():
#     cursor = db.cursor()
#     cursor.execute("SELECT temperature FROM weather_data WHERE date > DATE_SUB(CURDATE(), INTERVAL 1 WEEK)")
#     temperatures = cursor.fetchall()
#
#     plt.plot(temperatures)
#     plt.xlabel("Date")
#     plt.ylabel("Temperature (°C)")
#     plt.title("Historical Temperature Trends")
#     plt.show()
#
#
# def check_weather_alerts():
#     response = requests.get("https(://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY}")
#     data = response.json()
#     temperature = data["main"]["temp"]
#
#     cursor = db.cursor()
#     cursor.execute("SELECT alert_temperature FROM weather_alerts WHERE user_id = 1")
#     alert_temperature = cursor.fetchone()[0]
#     if temperature > alert_temperature:
#         print("Weather alert triggered!")
#
#
# root.mainloop()








import mysql.connector
import requests
import tkinter as tk
import matplotlib.pyplot as plt

# Define the API key
API_KEY = "b8c4038152a8f408402562a3328aef1a"

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
    CREATE TABLE IF NOT EXISTS weather_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        city VARCHAR(50) NOT NULL,
        temperature FLOAT NOT NULL,
        humidity FLOAT NOT NULL,
        description VARCHAR(100) NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        alert_temperature FLOAT,
        alert_humidity FLOAT,
        alert_description VARCHAR(100)
    )
"""
cursor.execute(query)

# Create the weather_alerts table
query = """
    CREATE TABLE IF NOT EXISTS weather_alerts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        city VARCHAR(50) NOT NULL,
        alert_temperature FLOAT NOT NULL,
        alert_humidity FLOAT NOT NULL,
        alert_description VARCHAR(100) NOT NULL
    )
"""
cursor.execute(query)

# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()

# Define a function to store historical weather data
def store_historical_weather_data(city, temperature, humidity, description):
    cnx = mysql.connector.connect(
        user='root',
        password='igetbacking24',
        host='localhost',
        database='weather_app'
    )
    cursor = cnx.cursor()
    query = """
        INSERT INTO weather_data (city, temperature, humidity, description)
        VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(query, (city, temperature, humidity, description))
    cnx.commit()
    cursor.close()
    cnx.close()

# Define a function to plot historical temperature trends
def plot_historical_trends(city):
    cnx = mysql.connector.connect(
        user='root',
        password='igetbacking24',
        host='localhost',
        database='weather_app'
    )
    cursor = cnx.cursor()
    query = """
        SELECT temperature FROM weather_data WHERE city = %s AND date > DATE_SUB(CURDATE(), INTERVAL 1 WEEK)
    """
    cursor.executemany(query, (city,))
    temperatures = cursor.fetchall()
    plt.plot([temp[0] for temp in temperatures])
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Historical Temperature Trends")
    plt.show()
    cursor.close()
    cnx.close()

# Define a function to check weather alerts
def check_weather_alerts(city):
    cnx = mysql.connector.connect(
        user='root',
        password='igetbacking24',
        host='localhost',
        database='weather_app'
    )
    cursor = cnx.cursor()
    query = """
        SELECT alert_temperature FROM weather_alerts WHERE city = %s
    """
    cursor.executemany(query, (city,))
    alert_temperature = cursor.fetchall()[0]
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}")
    data = response.json()
    temperature = data["main"]["temp"]
    if temperature > alert_temperature:
        print("Weather alert triggered!")
    cursor.close()
    cnx.close()

# Create a GUI for the weather app
root = tk.Tk()
root.title("Desktop Weather App")

# Create a label and entry field for the city
city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Create a button to store historical weather data
store_button = tk.Button(root, text="Store Historical Weather Data", command=lambda: store_historical_weather_data(city_entry.get()))
store_button.pack()

# Create a button to plot historical temperature trends
plot_button = tk.Button(root, text="Plot Historical Temperature Trends", command=lambda: plot_historical_trends(city_entry.get()))
plot_button.pack()

# Create a button to check weather alerts
alert_button = tk.Button(root, text="Check Weather Alerts", command=lambda: check_weather_alerts(city_entry.get()))
alert_button.pack()

root.mainloop()

# import mysql.connector
# import requests
# import tkinter as tk
# import matplotlib.pyplot as plt
# from datetime import datetime, timedelta
#
# # Define the API key
# API_KEY = "b8c4038152a8f408402562a3328aef1a"
#
#
#
# # Establish a connection to the database
# cnx = mysql.connector.connect(
#     user='root',
#     password='igetbacking24',
#     host='localhost',
#     database='weather_app'
# )
#
# # Create a cursor object to execute queries
# cursor = cnx.cursor()
#
# # Create the weather_data table
# query = """
#     CREATE TABLE IF NOT EXISTS weather_data (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         city VARCHAR(50) NOT NULL,
#         temperature FLOAT NOT NULL,
#         humidity FLOAT NOT NULL,
#         description VARCHAR(100) NOT NULL,
#         date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     )
# """
# cursor.execute(query)
#
# # Commit the changes
# cnx.commit()
#
# # Close the cursor and connection
# cursor.close()
# cnx.close()
#
# # Define a function to get current weather data
# def get_current_weather_data(city):
#     response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}")
#     data = response.json()
#     temperature = data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
#     humidity = data["main"]["humidity"]
#     description = data["weather"][0]["description"]
#     return temperature, humidity, description
#
# # Define a function to get past week's weather data
# def get_past_week_weather_data(city):
#     past_week_data = []
#     for i in range(7):
#         date = datetime.now() - timedelta(days=i+1)
#         response = requests.get(f"http://api.openweathermap.org/data/2.5/onecall/timemachine?q={city}&dt={int(date.timestamp())}&appid={API_KEY}")
#         data = response.json()
#         temperature = data["hourly"][0]["temp"] - 273.15  # Convert Kelvin to Celsius
#         humidity = data["hourly"][0]["humidity"]
#         description = data["hourly"][0]["weather"][0]["description"]
#         past_week_data.append((temperature, humidity, description))
#     return past_week_data
#
# # Define a function to store historical weather data
# def store_historical_weather_data(city, temperature, humidity, description):
#     cnx = mysql.connector.connect(
#         user='root',
#         password='igetbacking24',
#         host='localhost',
#         database='weather_app'
#     )
#     cursor = cnx.cursor()
#     query = """
#         INSERT INTO weather_data (city, temperature, humidity, description)
#         VALUES (%s, %s, %s, %s)
#     """
#     cursor.execute(query, (city, temperature, humidity, description))
#     cnx.commit()
#     cursor.close()
#     cnx.close()
#
# # Create a GUI for the weather app
# root = tk.Tk()
# root.title("Desktop Weather App")
#
# # Create a label and entry field for the city
# city_label = tk.Label(root, text="City:")
# city_label.pack()
# city_entry = tk.Entry(root)
# city_entry.pack()
#
# # Create a button to get current weather data and store it
# current_button = tk.Button(root, text="Get Current Weather Data", command=lambda:
#     store_historical_weather_data(city_entry.get(), *get_current_weather_data(city_entry.get())))
# current_button.pack()
#
# # Create a button to get past week's weather data and store it
# past_button = tk.Button(root, text="Get Past Week's Weather Data", command=lambda:
# [store_historical_weather_data(city_entry.get(), *data) for data in get_past_week_weather_data(city_entry.get())])
# past_button.pack()
#
# root.mainloop()



# import mysql.connector
# import requests
# import tkinter as tk
# from tkinter import messagebox
# import matplotlib.pyplot as plt
# from datetime import datetime, time
#
# # Define the API key
# API_KEY = "b8c4038152a8f408402562a3328aef1a"
#
# # Establish a connection to the database
# cnx = mysql.connector.connect(
#     user='root',
#     password='igetbacking24',
#     host='localhost',
#     database='weather_app'
# )
#
# # Create a cursor object to execute queries
# cursor = cnx.cursor()
#
# # Create the weather_data table
# query = """
#     CREATE TABLE IF NOT EXISTS weather_data (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         city VARCHAR(50) NOT NULL,
#         temperature FLOAT NOT NULL,
#         humidity FLOAT NOT NULL,
#         description VARCHAR(100) NOT NULL,
#         date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     )
# """
# cursor.execute(query)
#
# # Create the weather_alerts table
# query = """
#     CREATE TABLE IF NOT EXISTS weather_alerts (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         city VARCHAR(50) NOT NULL,
#         alert_temperature FLOAT NOT NULL,
#         alert_humidity FLOAT NOT NULL,
#         alert_description VARCHAR(100) NOT NULL
#     )
# """
# cursor.execute(query)
#
# # Commit the changes
# cnx.commit()
#
# # Close the cursor and connection
# cursor.close()
# cnx.close()
#
# # Define a function to get current weather data
# def get_current_weather_data(city):
#     response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}")
#     data = response.json()
#     temperature = data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
#     humidity = data["main"]["humidity"]
#     description = data["weather"][0]["description"]
#     return temperature, humidity, description
#
# # Define a function to store historical weather data
# def store_historical_weather_data(city, temperature, humidity, description):
#     cnx = mysql.connector.connect(
#         user='root',
#         password='igetbacking24',
#         host='localhost',
#         database='weather_app'
#     )
#     cursor = cnx.cursor()
#     query = """
#         INSERT INTO weather_data (city, temperature, humidity, description)
#         VALUES (%s, %s, %s, %s)
#     """
#     cursor.execute(query, (city, temperature, humidity, description))
#     cnx.commit()
#     cursor.close()
#     cnx.close()
#
# # Define a function to display current weather conditions
# def display_current_weather(city, current_weather_label=None):
#     temperature, humidity, description = get_current_weather_data(city)
#     current_weather_label.config(text=f"Current Weather in {city}:\nTemperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description}")
#
# # Define a function to display historical trends
# def display_historical_trends(city):
#     cnx = mysql.connector.connect(
#         user='root',
#         password='igetbacking24',
#         host='localhost',
#         database='weather_app'
#     )
#     cursor = cnx.cursor()
#     query = """
#         SELECT temperature FROM weather_data WHERE city = %s AND date > DATE_SUB(CURDATE(), INTERVAL 1 WEEK)
#     """
#     cursor.execute(query, (city,))
#     temperatures = cursor.fetchall()
#     plt.plot([temp[0] for temp in temperatures])
#     plt.xlabel("Date")
#     plt.ylabel("Temperature (°C)")
#     plt.title("Historical Temperature Trends")
#     plt.show()
#     cursor.close()
#     cnx.close()
#
# # Define a function to set weather alerts
# def set_weather_alert(city, alert_temperature, alert_humidity, alert_description):
#     cnx = mysql.connector.connect(
#         user='root',
#         password='igetbacking24',
#         host='localhost',
#         database='weather_app'
#     )
#     cursor = cnx.cursor()
#     query = """
#         INSERT INTO weather_alerts (city, alert_temperature, alert_humidity, alert_description)
#         VALUES (%s, %s, %s, %s)
#     """
#     cursor.execute(query, (city, alert_temperature, alert_humidity, alert_description))
#     cnx.commit()
#     cursor.close()
#     cnx.close()
#     messagebox.showinfo("Weather Alert", "Weather alert set successfully!")
#
# # Create a GUI for the weather app
# root = tk.Tk()
# root.title("Desktop Weather App")
#
# # Create a label and entry field for the city
# city_label = tk.Label(root, text="City:")
# city_label.pack()
# city_entry = tk.Entry(root)
# city_entry.pack()
#
# # Create a button to display current weather conditions
# current_button = tk.Button(root, text="Display Current Weather", command=lambda: display_current_weather(city_entry.get()))
# current_button.pack()
#
# # Create a button to display historical trends
# trends_button = tk.Button(root, text="Display Historical Trends", command=lambda: display_historical_trends(city_entry.get()))
# trends_button.pack()
#
# Create a label and entry fields for
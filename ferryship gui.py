# import requests
#
# API_KEY = "b8c4038152a8f408402562a3328aef1a"
# city_name = input("Enter the name of your state: ")
#  url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
# response = requests.get(url)
# data = response.json()
# print("The temperature of", city_name, "is: ", data["main"]["temp"])
# print("The humidity of", city_name, "is: ", data["main"]["humidity"])
# print("The description of", city_name, "is: ", data["weather"][0]["description"])
# print("The windspeed of", city_name, "is: ", data["wind"]["speed"])


# import tkinter as tk
# from tkinter import messagebox
# import requests
# from PIL import Image, ImageTk
# def get_weather():
#     city = city_entry.get()
#      API_key = "b8c4038152a8f408402562a3328aef1a"
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
#
#     weather_label.config(text="Loading...")
#     icon_label.config(image='')
#
#     response = requests.get(url)
#     weather_data = response.json()
#     if "message" in weather_data:
#         messagebox.showerror("Error", weather_data["message"])
#     else:
#         weather_text = f"City: {city}\n"
#         weather_text += f"Temperature: {weather_data['main']['temp']}°F\n"
#         weather_text += f"Pressure: {weather_data['main']['pressure']} hPa\n"
#         weather_text += f"Humidity: {weather_data['main']['humidity']}%\n"
#         weather_text += f"Min Temp: {weather_data['main']['temp_min']}°F\n"
#         weather_text += f"Max Temp: {weather_data['main']['temp_max']}°F\n"
#         weather_text += f"Wind Speed: {weather_data['wind']['speed']} m/s\n"
#         weather_text += f"Description: {weather_data['weather'][0]['description']}\n"
#         weather_text += f"Sunrise: {weather_data['sys']['sunrise']}\n"
#         weather_text += f"Sunset: {weather_data['sys']['sunset']}\n"
#         weather_label.config(text=weather_text)
#
#         icon_name = weather_data['weather'][0]['icon']
#         icon_url = f"http://openweathermap.org/img/wn/{icon_name}@2x.png"
#         icon_data = requests.get(icon_url)
#         with open("icon.png", "wb") as f:
#             f.write(icon_data.content)
#         icon_image = ImageTk.PhotoImage(Image.open("icon.png"))
#         icon_label.config(image=icon_image)
#         icon_label.image = icon_image
#
# root = tk.Tk()
# root.title("Weather App")
#
# gradient = Image.new("RGBA", (1, root.winfo_height()), "#8EC5FC")
# pixels = gradient.load()
# for y in range(gradient.size[1]):
#     color = int(y / gradient.size[1] * 255), 140, 255
#     for x in range(gradient.size[0]):
#         pixels[x, y] = color
# gradient = gradient.resize((root.winfo_width(), root.winfo_height()))
#
# gradient = ImageTk.PhotoImage(gradient)
#
# bg_label = tk.Label(root, image=gradient)
# bg_label.place(relx=0, rely=0, relheight=1, relwidth=1)
#
# frame = tk.Frame(root, bg='#80c1ff', bd=5)
# frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
#
# city_entry = tk.Entry(frame, font=("Courier", 15))
# city_entry.place(relwidth=0.65, relheight=1)
#
# tk.Button(frame, text="Get Weather", command=get_weather, font=("Arial", 10), bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5).place(relx=0.7, relwidth=0.3, relheight=1)
#
# weather_label = tk.Label(root, font=("Arial", 15), anchor='nw', justify='left')
# weather_label.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
#
# icon_label = tk.Label(root)
# icon_label.place(relx=0.5, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
#
# root.mainloop()



# import tkinter as tk
# import requests
#
# import tkinter as tk
# from tkinter import messagebox
# import requests
#
# def get_weather(city):
#     API_KEY = "b8c4038152a8f408402562a3328aef1a"
#     base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
#     response = requests.get(base_url)
#     data = response.json()
#     return data
#
# def display_weather(data):
#     temperature = data["main"]["temp"]
#     humidity = data["main"]["humidity"]
#     description = data["weather"][0]["description"]
#     temperature_label.config(text=f"Temperature: {temperature}°C")
#     humidity_label.config(text=f"Humidity: {humidity}%")
#     description_label.config(text=f"Description: {description}")
#
# def search_city():
#     city = city_entry.get()
#     data = get_weather(city)
#     display_weather(data)
#
# root = tk.Tk()
# root.title("Weather App")
#
# city_label = tk.Label(root, text="Enter City:")
# city_label.pack()
#
# city_entry = tk.Entry(root)
# city_entry.pack()
#
# search_button = tk.Button(root, text="Search", command=search_city)
# search_button.pack()
#
# temperature_label = tk.Label(root, text="Temperature:")
# temperature_label.pack()
#
# humidity_label = tk.Label(root, text="Humidity:")
# humidity_label.pack()
#
# description_label = tk.Label(root, text="Description:")
# description_label.pack()
#
# root.mainloop()
#



# import mysql.connector


# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="igetbacking24",
#
# )

#
# cursor = mydb.cursor[("CREATE TABLE weather_data"
# 	"id INT PRIMARY KEY AUTO_INCREMENT"
# 	"location VARCHAR(50)"
# 	"date DATE"
# 	"high_temperature FLOAT"
# 	"low_temperature FLOAT"
# 	"condition VARCHAR(50)"
# 	"precipitation FLOAT"
# 	"last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP")]

#
# cursor.execute("CREATE DATABASE weather_app")
#
#
# for db in cursor:
#   print(db)
#
# print(mydb)
#
# cursor = mydb.cursor()

# cursor.execute("create database employees")
# cursor.execute("show databases")
# cursor.execute("create table employeestb (name varchar(250),age integer, email varchar(250))")
# cursor.execute("show tables")
# sql = "insert into employeestb(name, age, email)value(%s, %s, %s)"
# employee1 = ("michael", 90, "pontuispilate@gmail.com")
# cursor.execute(sql, employee1)
#
# mydb.commit()
# for db in cursor:
#    print(db)




# import mysql.connector
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
#     CREATE TABLE weather_data (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         city VARCHAR(50) NOT NULL,
#         temperature FLOAT NOT NULL,
#         humidity FLOAT NOT NULL,
#         description VARCHAR(100) NOT NULL,
#         date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         alert_temperature FLOAT,
#         alert_humidity FLOAT,
#         alert_description VARCHAR(100)
#     )
# """
# cursor.execute(query)
#
# # Create the weather_alerts table
# query = """
#     CREATE TABLE weather_alerts (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         user_id INT NOT NULL,
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
#
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
#     plt.plot("temperatures")
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

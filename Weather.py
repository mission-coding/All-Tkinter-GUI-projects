import tkinter as tk
import requests

root = tk.Tk()
root.geometry("320x300")
root.title("Weather App")
root.resizable(False, False)

def weather():
    city_name = city_box.get()
    api_key = "56c11be3c15e81cf662e76423210264b"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    resonse = requests.get(url)
    data = resonse.json()
    # print(data)

    try:
        descrip_label.config(text="Description: "+str(data["weather"][0]["main"]))

        temp = data["main"]["temp"]
        temp_label.config(text=f"Temprature: {str(round(temp-273, 2))}°C")

        pressure = data["main"]["pressure"]
        pressure_label.config(text=f"Pressure: {str(pressure)} hPa")

        humid = data["main"]["humidity"]
        humid_label.config(text=f" Humidity: {str(humid)}%")

        wind_speed = data["wind"]["speed"]
        wind_speed_label.config(text=f" Wind Speed: {str(wind_speed)} m/s")

    except:
        isfound.config(text="City Not Found", fg="red")
        descrip_label.config(text="Description: ")
        temp_label.config(text="Temprature: ")
        pressure_label.config(text="Pressure: ")
        humid_label.config(text="Humidity: ")
        wind_speed_label.config(text="Wind Speed: ")


tk.Label(root, text=" Enter the City", font="Helvetica 14").pack()

f1 = tk.Frame(root)
f1.pack()

city_var = tk.StringVar()
city_box = tk.Entry(f1, textvariable="city_var", font="Helvetica 14")
city_box.pack(side="left")

find_button = tk.Button(f1, text="search", command=weather, font="Helvetica 14")
find_button.pack(side="right")

isfound = tk.Label(root, text="", font="Helvetica 14")
isfound.pack()

f2 = tk.Frame(root)
f2.pack(side="left", padx=20)

descrip_label = tk.Label(f2, text="Description: ", justify="left", font="Helvetica 14")
descrip_label.pack()

temp_label = tk.Label(f2, text="Temprature: ", justify="left", font="Helvetica 14")
temp_label.pack()

pressure_label = tk.Label(f2, text="Pressure: ", justify="left", font="Helvetica 14")
pressure_label.pack()

humid_label = tk.Label(f2, text="Humidity: ", justify="left", font="Helvetica 14")
humid_label.pack()

wind_speed_label = tk.Label(f2, text="Wind Speed: ", justify="left", font="Helvetica 14")
wind_speed_label.pack()

root.mainloop()
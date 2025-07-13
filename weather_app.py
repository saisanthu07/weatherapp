import requests
import tkinter as tk
from tkinter import messagebox

# Replace this with your actual OpenWeatherMap API key
API_KEY = "279e0e56d484f618d6a39de15104dd1b"

def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", data["message"])
            return

        city_name = data["name"]
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result = f"City: {city_name}\nTemperature: {temp}°C\nCondition: {description}\nHumidity: {humidity}%\nWind Speed: {wind} m/s"
        result_label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get data\n{e}")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.config(bg="#e0f7fa")

tk.Label(root, text="Enter City Name:", font=("Arial", 14), bg="#e0f7fa").pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14), justify='center')
city_entry.pack()

tk.Button(root, text="Get Weather", font=("Arial", 12), bg="#4fc3f7", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#e0f7fa", justify="left")
result_label.pack(pady=10)

root.mainloop()

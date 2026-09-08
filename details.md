# 🌦️ Weather Analyzer

A beginner-friendly Python project that fetches current weather data for a city using the **Open-Meteo API** and performs basic weather analysis using Python conditional statements.

This project was created to practice **Python, APIs, JSON data, functions, and error handling**.

## 📌 Features

The Weather Analyzer takes a city name from the user and provides:

* 🌡️ Current temperature
* 🌡️ Feels-like temperature
* 💧 Relative humidity
* 🌧️ Current precipitation
* 🌧️ Current rainfall
* 💨 Wind speed
* 🧭 Wind direction

It then analyzes the weather conditions and categorizes:

* Temperature
* Humidity
* Rainfall
* Wind speed

## 🛠️ Technologies Used

* **Python**
* **Requests** library
* **Open-Meteo Geocoding API**
* **Open-Meteo Weather API**
* JSON
* Conditional statements (`if`, `elif`, `else`)
* Functions
* Exception handling

## ⚙️ How It Works

The program follows these basic steps:

```text
Enter City
     ↓
Geocoding API
     ↓
Get Latitude & Longitude
     ↓
Weather API
     ↓
Get Current Weather Data
     ↓
Extract Weather Information
     ↓
Analyze Weather
     ↓
Display Results
```

### 1. Enter a city

The user enters the name of a city.

### 2. Find the location

The Open-Meteo Geocoding API is used to find the city's latitude and longitude.

### 3. Get weather data

The latitude and longitude are passed to the Open-Meteo Forecast API to retrieve current weather information.

### 4. Analyze the data

Python `if-elif-else` statements are used to categorize the weather.

For example:

```python
if temperature <= 10:
    print("Temperature is too Cold")
elif temperature <= 20:
    print("Temperature is Cool")
elif temperature <= 30:
    print("Temperature is comfortable")
elif temperature <= 40:
    print("It will be hot outside")
else:
    print("Very Hot Outside")
```

## 📊 Weather Analysis

### Temperature

The temperature is categorized as:

* Too Cold
* Cool
* Comfortable
* Hot
* Very Hot

### Humidity

Humidity is categorized as:

* Dry
* Comfortable
* Humid
* Very Humid

### Rain

Rainfall is analyzed using its amount in **millimeters (mm)**:

* No Rain
* Light Rain
* Moderate Rain
* Heavy Rain

### Wind

Wind speed is categorized as:

* Calm
* Light Breeze
* Moderate Wind
* Strong Wind
* Very Strong Wind

## 🚨 Error Handling

The program includes basic exception handling for:

* Internet connection problems
* HTTP/API request errors
* Invalid or unavailable city results
* Missing location data

Example:

```python
except requests.exceptions.ConnectionError:
    print("Internet connection problem!")
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install Requests

Open your terminal and run:

```bash
pip install requests
```

### 3. Run the program

```bash
python main.py
```

### 4. Enter a city

Example:

```text
Enter Your City : Prayagraj
```

The program will then display the current weather and its analysis.

## 🖥️ Example Output

```text
==============WEATHER==============
Enter Your City : Prayagraj
Your City : Prayagraj

Temperature : 29 °C
Humidity : 65 %
Feels Like : 31 °C
Precipitation : 0.0 mm
Rain : 0.0 mm
Wind Speed : 12 km/h
Wind Direction : 180°

WEATHER ANALYSIS
-----------------------------------
Analysing Weather !
==============================

Temperature is comfortable
Humid outside
No Rain currently
Light breeze
========================================
```

*The values in this example are only for demonstration and will change depending on the city and current weather.*

## 🎯 What I Learned

Through this project, I practiced:

* Taking user input in Python
* Making API requests using `requests`
* Working with REST APIs
* Reading and extracting data from JSON
* Accessing nested dictionaries
* Using functions
* Applying `if-elif-else` logic
* Basic exception handling
* Working with real-world data

## 🔮 Future Improvements

Possible improvements for future versions:

* Add weather conditions using weather codes
* Add precipitation probability
* Allow users to select between multiple matching cities
* Add more weather parameters
* Improve error handling
* Add a reusable function-based structure
* Add weather forecasts for upcoming days

## 📚 APIs Used

This project uses the free **Open-Meteo API**:

* Geocoding API — to find latitude and longitude from a city name
* Forecast API — to retrieve current weather information

## 👨‍💻 Project Status

**Completed — Beginner Python Project**

This project was created as part of my journey to improve my Python and data-handling skills.

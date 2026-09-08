import requests
import time
try:
    print("==============WEATHER==============")
    city=input("Enter Your City : ")
    print(f"Your City : {city}")
    

    #getting the longitudes and lattitudes
    url1=f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json"
    city_details=requests.get(url1)
    data1=city_details.json()
    latiude=data1["results"][0]["latitude"]
    longitude=data1["results"][0]["longitude"]
    

    #putting url1 data to get weather details
    url=f"https://api.open-meteo.com/v1/forecast?latitude={latiude}&longitude={longitude}&current=relative_humidity_2m,temperature_2m,apparent_temperature,weather_code,precipitation,rain,wind_speed_10m,wind_direction_10m"
    # print(url)
    
    

    #getting weather details
    weather_details=requests.get(url)
    data2=weather_details.json()
    humidity=data2["current"]["relative_humidity_2m"]
    temperature=data2["current"]["temperature_2m"]
    feellike=data2["current"]["apparent_temperature"]
    precipitation=data2["current"]["precipitation"]
    rain=data2["current"]["rain"]
    wind_speed=data2["current"]["wind_speed_10m"]
    wind_direction=data2["current"]["wind_direction_10m"]


    def print_details():
        print(f"Temprature : {temperature} °C")
        print(f"Humidity : {humidity} %")
        print(f"Feels Like : {feellike} °C ")
        print(f"Precipitation: {precipitation} mm")
        print(f"Rain : {rain} mm")
        print(f"Wind Speed : {wind_speed} km/h")
        print(f"Wind direction : {wind_direction} °")

    print_details()
    print("WEATHER ANALYSIS")
    print("-----------------------------------")
    print("Analysing Weather !\n==============================")
    time.sleep(3)

    #weather analysis
    #for temprature
    
    if(temperature)<=10:
        print("Temprature is too Cold")
    elif temperature<=20 and temperature>10:
        print("Temprature is Cool")
    elif temperature<=30 and temperature>20:
        print("Temprature is comfortable")
    elif temperature<=40 and temperature>30:
        print("It will be hot outside")
    elif temperature > 40:
        print("Very Hot Outside")
    else:
        print("Cant Predict")


    #for humidity
    if(humidity) <=30:
        print("It feels like Dry")
    elif humidity >30 and humidity <=60:
        print("Humidity is comfortable")
    elif humidity >60 and humidity <=75:
        print("Humid outside")
    elif humidity >75:
        print("Very Humid Outside")
    else:
        print("Cant Guess!")


    #for rain 
    if rain >=0 and rain <1:
        print("No Rain currently")
    elif rain < 2.5:
        print("Light Rain")
    elif rain >=2.5 and rain <7.4:
        print("Moderate Rain")
    elif rain >=7.4:
        print("Heavy Rain")
    else :
        print("Cant Predict")

    #for wind speed 

    if wind_speed < 5:
        wind_status = "Calm"
    elif wind_speed < 20:
        wind_status = "Light breeze"
    elif wind_speed < 40:
        wind_status = "Moderate wind"
    elif wind_speed < 60:
        wind_status = "Strong wind"
    else:
        wind_status = "Very strong wind"
    print(wind_status)     
    print("========================================")

except requests.exceptions.HTTPError:
    print("API request failed.")
except requests.exceptions.ConnectionError:
    print("Internet connection problem!")

except KeyError:
    print("City Not Found. Try entering another city !")
except IndexError:
    print("No Location found for this city")



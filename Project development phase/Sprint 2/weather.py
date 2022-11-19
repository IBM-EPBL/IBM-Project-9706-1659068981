#weather function

def get_whether():
    api_key = "b48129c70234f815d857006719283786"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Coimbatore"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
#     print(x)
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
#         print(" Temperature (in kelvin unit) = " + str(current_temperature))
#         print(" Atmospheric pressure (in hPa unit) = " +str(current_pressure)) 
#         print(" Humidity (in percentage) = " + str(current_humidity))
#         print(" Description = " + str(weather_description))
        return(current_temperature,current_pressure,current_humidity,weather_description)
    else:
        print(" City Not Found ")

    current_temperature,current_pressure,current_humidity,weather_description = get_whether()
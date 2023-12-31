import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    city_format = city.lower().replace(' ', '+')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=e9926d9cabaa85df3a3592b64a40691b&units=metric'.format(city_format)
    request = requests.get(url)
    data = request.json()

    temp = int(data['main']['temp'])
    wind_speed = data['wind']['speed']
    wind_dir = data['wind']['deg']
    humidity = data['main']['humidity']
    high = int(data['main']['temp_max'])
    low = int(data['main']['temp_min'])
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

    def wind_direction_convert(degree):
        if degree >= 337.501 or degree <= 22.5:
            wind_direction = 'North'
        elif degree >= 22.501 and degree <= 65.5:
            wind_direction = 'Northeast'
        elif degree >= 65.501 and degree <= 112.5:
            wind_direction = 'East'
        elif degree >= 112.501 and degree <= 157.5:
            wind_direction = 'Southeast'
        elif degree >= 157.501 and degree <= 202.5:
            wind_direction = 'South'
        elif degree >= 202.501 and degree <= 247.5:
            wind_direction = 'Southwest'
        elif degree >= 247.501 and degree <= 292.5:
            wind_direction = 'West'
        else:
            wind_direction = 'Northwest'
        return wind_direction

    result_label.config(text='*~*~*~' + city + '~*~*~*' +
                             '\nThe current temperature is: {}°C'.format(temp) +
                             '\nThe local high is: {}°C'.format(high) +
                             '\nThe local low is: {}°C'.format(low) +
                             '\nThe wind speed is: {} mph'.format(wind_speed) +
                             '\nThe wind direction is: {}'.format(wind_direction_convert(wind_dir)) +
                             '\nThe humidity is: {}%'.format(humidity) +
                             '\nThe locational coordinates for {} are: ({:.2f}, {:.2f})'.format(city, latitude, longitude))

# Create the main window
root = tk.Tk()
root.title('Weather App')

# Create input and output elements
city_label = tk.Label(root, text='Enter a valid city:')
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()
get_weather_button = tk.Button(root, text='Get Weather', command=get_weather)
get_weather_button.pack()

result_label = tk.Label(root, text='', wraplength=300)
result_label.pack()

# Start the main event loop
root.mainloop()
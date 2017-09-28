import pyowm

owm = pyowm.OWM('9d0f3754a60b7fd3c1ff4db441e8c898')
observation = owm.weather_at_place('London')
w = observation.get_weather()

temperatura = w.get_temperature('celsius')['temp']

print('Temperatura ' + str(temperatura) + ' po C and status ' + str(w.get_detailed_status()))
import json

WEATHER_PATH = 'weather.json'

with open(WEATHER_PATH) as file:
    weather = json.load(file)

rows = [
    weather['name'],
    '-' * 15,
    weather['weather'][0]['main'],
    f"Current temperature {weather['main']['temp']} C",
    f"Minimum temperature {weather['main']['temp_min']} C",
    f"Maximum temperature {weather['main']['temp_max']} C",
    f"Wind speed          {weather['wind']['speed']} m/s",
]

max_length = max(len(row) for row in rows)

rows.insert(0, '#' * max_length)
rows.append('#' * max_length)

for row in rows:
    print(row)

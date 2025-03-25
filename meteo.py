import pandas as pd
data = pd.read_json('meteo.json')
weather_days = []
for day_key in [f"day{i}" for i in range(1, 8)]:
    day_data = data[day_key]
    weather_days.append({
        "date": day_data["date"],
        "temperature_max": day_data["temperature_max"],
        "temperature_min": day_data["temperature_min"],
        "humidity": day_data["humidity"]
    })
df = pd.DataFrame(weather_days)
df["date"] = pd.to_datetime(df["date"])
print(df)


import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["temperature_max"], 
         marker='o', label="Temperatura Massima (°C)", color="tab:red")
plt.plot(df["date"], df["temperature_min"], 
         marker='o', label="Temperatura Minima (°C)", color="tab:blue")

plt.fill_between(df["date"],
                 df["temperature_max"],
                 df["temperature_min"])

plt.show()
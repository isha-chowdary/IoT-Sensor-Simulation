import random
import time
import pandas as pd

# List to store simulated readings
data = []

# Simulate 20 sensor readings
for i in range(20):
    temp = round(random.uniform(20, 35), 2)  # temperature between 20-35°C
    timestamp = time.strftime('%H:%M:%S')
    data.append([timestamp, temp])
    print(f"{timestamp} - {temp}°C")
    time.sleep(1)  # wait 1 second between readings

# Save data to CSV
df = pd.DataFrame(data, columns=["Time", "Temperature"])
df.to_csv("temperature_data.csv", index=False)
print("Simulation complete! Data saved to temperature_data.csv")
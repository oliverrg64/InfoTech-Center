import random
from time import sleep

print("\n***********************************\nGasoline Branch - Developer: Oliver Gibbs\n")

fuel = random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three-Quarter Tank", "Full Tank"])
stations = ['Shell', 'Marathon', 'Speedway', 'Circle K', 'Wesco', 'Meijer', 'Buc-ees', 'Sam\'s Club', 'Costco']

def alert(f, miles=None):
    sleep(1.25)
    print(f, f"Nearest: {random.choice(stations)} {miles} miles.\n" if miles else '')

if fuel == "Empty": alert("*****WARNING - FUEL TANK FULLY DEPLETED*****\n"); print("Alerting AAA")
elif fuel in ["Low", "Quarter Tank"]: alert(f"Warning - {fuel} fuel - Setting GPS route", round(random.uniform(1,50),1))
else: alert(f"Warning - {fuel} fuel - Refill not needed.\n" if fuel != "Full Tank" else "Full tank, drive safe!\n")

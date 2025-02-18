import random  # Importing random module to generate random choices
from time import sleep  # Importing sleep function to simulate delays

# Printing the header information
print("\n***********************************\nGasoline Branch - Developer: Oliver Gibbs\n")

# Randomly choosing a fuel level from the list
fuel = random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three-Quarter Tank", "Full Tank"])

# List of available gas stations
stations = ['Shell', 'Marathon', 'Speedway', 'Circle K', 'Wesco', 'Meijer', 'Buc-ees', 'Sam\'s Club', 'Costco']

# Function to simulate alert with a sleep delay and print the alert message
def alert(f, miles=None):
    sleep(1.25)  # Simulate delay before showing the alert
    # Print the alert message, and if miles is provided, show the nearest gas station and distance
    print(f, f"Nearest: {random.choice(stations)} {miles} miles.\n" if miles else '')

# Checking the fuel level and taking appropriate action
if fuel == "Empty":
    alert("*****WARNING - FUEL TANK FULLY DEPLETED*****\n")  # Alert for empty tank
    print("Alerting AAA")  # Inform that AAA is being alerted
elif fuel in ["Low", "Quarter Tank"]:
    # Alert for low or quarter tank and set GPS route to nearest gas station
    alert(f"Warning - {fuel} fuel - Setting GPS route", round(random.uniform(1, 50), 1))
else:
    # Alert for other fuel levels, informing whether a refill is needed or not
    alert(f"Warning - {fuel} fuel - Refill not needed.\n" if fuel != "Full Tank" else "Full tank, drive safe!\n")

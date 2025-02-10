print("\n***********************************\n")

print("Weather Branch - Developer: Oliver Gibbs\n")

#Import Libraries Here!
import random
from time import sleep

# Weather Function to determine the weather
def weather():
    weatherForecastList = ["snowy", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because of the forecast of", weatherAlert, "weather condition")

    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because of the forecast of a", weatherAlert)

vehicleResponseSystem()
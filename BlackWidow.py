# Print a divider and header for better readability
print("\n***********************************\n")
print("Weather Branch - Developer: Oliver Gibbs\n")

# Import Libraries Here!
import random  # For generating random weather conditions
from time import sleep  # Import sleep in case you want to add delays later

# Weather Function to determine the weather
def weather():
    # A list of possible weather conditions
    weatherForecastList = ["snowy", "blizzard", "icy", "rainy", "windy", "sunny"]
    
    # Select a random weather condition from the list
    weatherCondition = random.choice(weatherForecastList)
    
    # Return the selected weather condition
    return weatherCondition

# Call the weather function and store the result in the variable 'weatherAlert'
weatherAlert = weather()

# Define a function to respond to the weather conditions and update the vehicle's alarm time
def vehicleResponseSystem():
    # Check which weather condition is returned and adjust alarm time accordingly
    if weatherAlert == "snowy":
        # If the weather is snowy, extend the alarm time by 30 minutes
        print("\nThe National Weather Service has updated your alarm by 30 minutes because of the forecast of", weatherAlert, "weather conditions.")
    elif weatherAlert == "blizzard":
        # If the weather is a blizzard, extend the alarm time by 60 minutes
        print("\nThe National Weather Service has updated your alarm by 60 minutes because of the forecast of a", weatherAlert,"in your area.")
    elif weatherAlert == "icy":
        # If the weather is icy, extend the alarm time by 90 minutes
        print("\nThe National Weather Service has updated your alarm by 90 minutes because of the forecast of", weatherAlert, "weather conditions.")
    elif weatherAlert == "rainy":
        # If the weather is rainy, extend the alarm time by 10 minutes
        print("\nThe National Weather Service has updated your alarm by 10 minutes because of the forecast of", weatherAlert, "weather conditions.")
    elif weatherAlert == "windy":
        # If the weather is windy, extend the alarm time by 5 minutes
        print("\nThe National Weather Service has updated your alarm by 5 minutes because of the forecast of", weatherAlert, "weather conditions.")
    else:
        # If the weather is sunny or any other condition, no alarm update is needed
        print("\nThe National Weather Service has forecasted", weatherAlert, "weather conditions. Alarm update not needed. Drive safe!")

# Call the vehicleResponseSystem function to display the result
vehicleResponseSystem()
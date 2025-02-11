
# Import necessary libraries
import sys  # For controlling the terminal output (like updating the message on the same line)
import time  # For adding delays (like in the loading process)

# ANSI escape codes for rainbow colors
RED = "\033[31m"  # Red color
GREEN = "\033[32m"  # Green color
YELLOW = "\033[33m"  # Yellow color
BLUE = "\033[34m"  # Blue color
MAGENTA = "\033[35m"  # Magenta color
CYAN = "\033[36m"  # Cyan color
RESET = "\033[0m"  # Reset color to default

# List of rainbow colors
RAINBOW_COLORS = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]

# Print a welcome message with developer information (in green)
print(GREEN + "Welcome Branch - Developer: Oliver Gibbs" + RESET)

# Print the name and version of the system (in yellow)
print(YELLOW + "\n\tWelcome to InfoTechCenter V1.0\n\n" + RESET)

# Initialize variables
x = 0  # Counter for the number of loading iterations
ellipsis = 0  # Counter for the number of dots added to the loading message

# Loop to simulate system booting (runs 20 iterations for the loading effect)
while x != 20:
    x += 1  # Increment the loop counter
    
    # Cycle through rainbow colors for the loading message
    color = RAINBOW_COLORS[ellipsis % len(RAINBOW_COLORS)]  # Select a color based on the ellipsis
    
    # Create a loading message with an increasing number of dots (colored with the selected rainbow color)
    message = (color + "InfoTech Center System Booting" + "." * ellipsis + RESET)
    
    # Increment the ellipsis counter to add another dot to the message
    ellipsis += 1
    
    # Write the message to the terminal, overwriting the previous one (in the rainbow color)
    # This creates the effect of a dynamic progress bar by updating the line in place
    sys.stdout.write("\r" + message)
    
    # Pause for half a second to simulate a loading delay
    time.sleep(0.5)
    
    # Reset the ellipsis counter after 4 dots (to create a looping effect for the dots)
    if ellipsis == 4:
        ellipsis = 0
    
    # Once the loop reaches 20 iterations, print the final success message (in green)
    # This indicates the system has successfully booted
    if x == 20:
        print(GREEN + "\nOperating System Booted up - Retina Scanned - Access Granted" + RESET)

import random
from time import sleep

# Print a divider and header for better readability
print("\n***********************************\n")
print("Weather Branch - Developer: Oliver Gibbs\n")

# Import Libraries Here!
import random  # For generating random weather conditions
from time import sleep  # Import sleep in case you want to add delays later


# Weather function to determine the weather
def weather():

    return random.choice(["snowy", "blizzard", "icy", "rainy", "windy", "sunny"])

# Dictionary to map weather conditions to alarm time and speed
weather_responses = {
    "snowy": (30, 60),
    "blizzard": (60, 55),
    "icy": (90, 45),
    "rainy": (10, 70),
    "windy": (5, 75),
    "sunny": (0, 0),
}

# Get the current weather condition
weather_alert = weather()

# Fetch the alarm time and speed from the dictionary
alarm_time, speed = weather_responses.get(weather_alert, (0, 0))

# Print appropriate response based on weather condition
if alarm_time > 0:
    print(f"\nThe National Weather Service has updated your alarm by {alarm_time} minutes because of {weather_alert} conditions.")
    print(f"VRS has been engaged, and the vehicle's speed limit is set to {speed} MPH.")
else:
    print(f"\nThe National Weather Service has forecasted {weather_alert} weather conditions. Alarm update not needed. Drive safe!")
    print("VRS has not been engaged - Travel Speed Limitations deactivated")

    # A list of possible weather conditions
    weatherForecastList = ["snowy", "blizzard", "icy", "rainy", "windy", "sunny"]
    
    # Select a random weather condition from the list
    weatherCondition = random.choice(weatherForecastList)


# Call the weather function and store the result in the variable 'weatherAlert'
weatherAlert = weather()


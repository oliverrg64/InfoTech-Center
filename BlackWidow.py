# Import necessary libraries
import sys  # For controlling the terminal output (like updating the message on the same line)
import time  # For adding delays (like in the loading process)

# Print a welcome message with developer information
print("Welcome Branch - Developer: Oliver Gibbs")

# Print the name and version of the system
print("\n\tWelcome to InfoTechCenter V1.0\n\n")

# Initialize variables
x = 0  # Counter for the number of loading iterations
ellipsis = 0  # Counter for the number of dots added to the loading message

# Loop to simulate system booting
while x != 20:
    x += 1  # Increment the loop counter
    
    # Create a loading message with an increasing number of dots
    message = ("InfoTech Center System Booting" + "." * ellipsis)
    
    # Increment the ellipsis counter to add another dot
    ellipsis += 1
    
    # Write the message to the terminal, overwriting the previous one
    sys.stdout.write("\r" + message)
    
    # Pause for half a second to create a delay
    time.sleep(0.5)
    
    # Reset the ellipsis counter after 4 dots (i.e., a full cycle of 4 dots)
    if ellipsis == 4:
        ellipsis = 0
    
    # When the loop reaches 20 iterations, print the final success message
    if x == 20:
        print("\nOperating System Booted up - Retina Scanned - Access Granted")

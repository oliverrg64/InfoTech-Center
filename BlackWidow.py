print("\n***********************************\n")
print("Gasoline Branch - Developer: Oliver Gibbs\n")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three-Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["Shell","Marathon","Speedway","Circle K","Wesco","Meijer","Buc-ees","Sam's Club","Costco"]
    return random.choice(gasStationsList)

print(gasLevelGauge())
print(gasStations())

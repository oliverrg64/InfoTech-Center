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

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("*****WARNING - FUEL TANK FULLY DEPLETED*****\n")
        sleep(1.25)
        print("Alerting AAA")
    elif gasLevelIndicator == "Low":
        print("Warning - Low Fuel - Setting GPS route to nearest gas station\n")
        sleep(1.25)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.\n")
    elif gasLevelIndicator == "Quarter Tank":
        print("Warning - Fuel levels nearing low levels - Setting GPS route to nearest gas station.\n")
        sleep(1.25)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.\n")
    elif gasLevelIndicator == "Half Tank":
        print("Warning - Fuel levels at 50 Percent - Gas refill not needed yet.\n")
    elif gasLevelIndicator == "Three-Quarter Tank":
        print("Warning - Fuel levels at 75 Percent - Gas refill not needed yet.\n")
    else:
        print("Your gas tank is full, Drive safe!\n")

gasLevelAlert()

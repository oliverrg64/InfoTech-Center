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
        print("Warning - Low Fuel - Setting GPS route to nearest gas station")
        sleep(1.25)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "QuarterTank":
        print("Warning - Fuel levels nearing low levels - Setting GPS route to nearest gas station")
        sleep(1.25)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half":
        print("Warning - Fuel levels at 50% - Gas refill not needed yet.")
    elif gasLevelIndicator == "ThreeQuarterTank":
        print("Warning - Fuel levels at 75% - Gas refill not needed yet")
    else:
        print("Your gas tank is full, Drive safe!")

gasLevelAlert()

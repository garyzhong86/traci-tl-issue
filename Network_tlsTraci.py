import os
import shutil
import sys
import optparse
import random
import numpy as np
import matplotlib.pyplot as plt
import subprocess
from subprocess import Popen,PIPE
from xml.etree import ElementTree as et
import pylab
import pandas as pd

# import lxml.etree as et # use lxml instead to preserve comments during writing

from sumolib import checkBinary  # Checks for the binary in environ vars
import traci


if __name__ == "__main__":
    currentLoc = os.getcwd()
    print(currentLoc)
    configFile = r'Network_tlsTraci.sumocfg'
    networkFile =r'Network_tlsTraci.net.xml'

    useGUI = True     #True
    if useGUI is False:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')
    traci.start([sumoBinary, "-c", configFile])

# Simulation Parameters
    simTime = 200 # simulation time, second
    simRes= 10
    totalTimeStep = simTime * simRes
    obserInterval = 30
    ts = 0

    signalMonitorList = []
    while ts <= totalTimeStep:
        traci.simulationStep()
        if (ts == 230):

            phases = []
            phases.append(traci.trafficlight.Phase(15, "rrrrGGGGrrr", 0, 0, [1,2,3], "setViaComplete"))
            phases.append(traci.trafficlight.Phase(2, "rrrryyyyrrr", 0, 0))
            phases.append(traci.trafficlight.Phase(7, "rrrrrrrrGGG", 0, 0))
            phases.append(traci.trafficlight.Phase(11, "rrrGGrrGGG", 0, 0))
            phases.append(traci.trafficlight.Phase(5, "rrrrrrrrGGy", 0, 0))
            phases.append(traci.trafficlight.Phase(6, "rrrrrrrrGGr", 0, 0))
            phases.append(traci.trafficlight.Phase(8, "GGGGrrrrGGr", 0, 0))
            phases.append(traci.trafficlight.Phase(2, "yyyyrrrryyr", 0, 0))
            phases.append(traci.trafficlight.Phase(1, "rrrrrrrrrrr", 0, 0))
            logic = traci.trafficlight.Logic("2117", 0, 0, phases)
            traci.trafficlight.setCompleteRedYellowGreenDefinition('2117', logic)
        ts += 1
    traci.close()

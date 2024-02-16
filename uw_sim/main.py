#!/usr/bin/env python3l
# -*- coding: utf-8 -*-
"""
main.py: Main program for the Python Vehicle Simulator, which can be used
    to simulate and test guidance, navigation and control (GNC) systems.

Reference: T. I. Fossen (2021). Handbook of Marine Craft Hydrodynamics and
Motion Control. 2nd edition, John Wiley & Sons, Chichester, UK. 
URL: https://www.fossen.biz/wiley  
    
Author:     Thor I. Fossen
"""
import os
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
from python_vehicle_simulator.vehicles import *
from python_vehicle_simulator.lib import *

# Simulation parameters: 
sampleTime = 0.02                   # sample time [seconds]
N = 10000                           # number of samples

# 3D plot and animation parameters where bindexser = {firefox,chrome,safari,etc.}
numDataPoints = 50                  # number of 3D data points
FPS = 10                            # frames per second (animated GIF)
filename = '3D_animation.gif'       # data file for animated GIF
eta = np.array([0, 0, 0, 0, 0, 0], float)    # position/attitude, user editable

###############################################################################
# Vehicle constructors
###############################################################################
printSimInfo() 

"""
remus100('depthHeadingAutopilot',z_d,psi_d,n_d,V_c,beta_c)
Parameters:
        z_d:desired depth (m), positive downwards
        psi_d:  desired yaw angle (deg)
        n_d:    desired propeller revolution (rpm)
        V_c:    current speed (m/s)
        beta_c: current direction (deg)
        1 knots = 1.852 km/hr
        1 knots = 0.514444 m/s    
        fl = input_data from profile_data.csv file
        k = d * r * 0.001885 Where,
        r = k / (20 * 0.001885) = k / 0.0377
        k = Kilometer Per Hour (km/hr) 
        d = Wheel Diameter (cm)
        r = Revolution Per Minute (RPM)
        d = diameter of propeller (cm)
        mps = meter per seconds

Call constructors without arguments to test step inputs, e.g. DSRV(), otter(), etc. 
"""

in_d = pd.read_csv("C:\\Users\\bhuva\\Documents\\controlsys\\Launchtrax_sim\\uw_sim\\New_profile.csv")

# array = in_d.values
# print(array)

# meter = in_d.iloc[:,1]
# z_d1 = meter * 0.3048
# psi_d1 = in_d.iloc[:,2]
# knots = in_d.iloc[:,3]
# km = knots * 1.852
# mps = knots * 0.51444
# n_d1 = (km / 0.0377)

# vehicle = remus100('depthHeadingAutopilot',30,50,1525,0.5,170)     
vehicle = remus100('depthHeadingAutopilot',22.86,25,1525,1.02889,170)   
printVehicleinfo(vehicle, sampleTime, N) 

###############################################################################
# Main simulation loop 
###############################################################################
def main():    

    [simTime, simData] = simulate(N, sampleTime, vehicle)

    # Append data to the SimData_Output.csv file
    # try block is used to check the SimData_Output data is writable to the SimData_Output file
    # if not available ,it will raise an exception
    # reset the SimData_Output.csv file
    with open("C:\\Users\\bhuva\\Documents\\controlsys\\Launchtrax_sim\\uw_sim\\SimData_Output.csv",'w',newline='') as file:
        pass

    try:
        with open("C:\\Users\\bhuva\\Documents\\controlsys\\Launchtrax_sim\\uw_sim\\SimData_Output.csv",'a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(simData[0])
            for row in simData[1:]:
                writer.writerow(row)

            # convert the matrix to a pandas dataframe
            # df = pd.DataFrame(simData)
            # writer.writerow(df)
            # for row in df[1:]:
            #     writer.writerow(row)
            #     writer.writerow(row)

    except IOError:
        print ("Cannot write the data into the file'SimData_Output.csv'")
#########################################################################################################################################        

    with open("C:\\Users\\bhuva\\Documents\\controlsys\\Launchtrax_sim\\uw_sim\\SimTime_Output.csv",'w',newline='') as file:
        pass

    try:
        with open("C:\\Users\\bhuva\\Documents\\controlsys\\Launchtrax_sim\\uw_sim\\SimTime_Output.csv",'a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(simTime[0])

            for row in simTime[1:]:
                writer.writerow(row)

    except IOError:
        print ("Cannot write the data into the file'SimTime_Output.csv'")

    # for i in range(len(in_d)):

    #     z_d = in_d.iloc[i,0] # Depth
    #     psi_d = in_d.iloc[i,1] # Heading angle
    #     n_d = in_d.iloc[i,2] # RPM
    #     V_c = in_d.iloc[i,3] # water_current_speed
    #     beta_c = in_d.iloc[i,4] # water_current_direction
    #     vehicle.nu = remus100('depthHeadingAutopilot',z_d,psi_d,n_d,V_c,beta_c)

    simD_path = pd.read_csv("C:\\Users\\bhuva\\Documents\\controlsys\\Launchtrax_sim\\uw_sim\\SimData_Output.csv")
    # simT_path = pd.read_csv("C:\\Users\\bhuva\\Documents\\controlsys\\Launchtrax_sim\\uw_sim\\SimTime_Output.csv")

    try:
        # vehicle.eta = simD_path.iloc[-1,0:7]
        # print(vehicle.eta)
        # vehicle.nu = simD_path.iloc[-1,7:13]
        # vehicle.u_actual = simD_path.iloc[-1,12:15]
        # vehicle.u_control = simD_path.ilco[-1,15:18]
        ########################################################################
        simData = simD_path.iloc[-1,:]
        # print(simData)
        # simTime = simT_path.iloc[-1,:]
        # print(simTime)
        vehicle1= remus100('depthHeadingAutopilot',45.72,70,1525,1.02889,170)
        [simTime, simData] = simulate(N, sampleTime, vehicle)
        try:
            with open("C:\\Users\\bhuva\\Documents\\controlsys\\Launchtrax_sim\\uw_sim\\SimData_Output.csv",'a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(simData[0])
                for row in simData[1:]:
                    writer.writerow(row)
        except IOError:
            print ("Cannot write the data into the file'SimData_Output.csv'")

    except Exception as e:
        print("CSV file is empty",e)

    # print("simdata:",simData.shape)

            
    # plotVehicleStates(simTime, simData, 1)                    
    # plotControls(simTime, simData, vehicle, 2)
    # final_sim = pd.read_csv("C:\\Users\\bhuva\\Documents\\controlsys\\Launchtrax_sim\\uw_sim\\SimData_Output.csv")
    # df = pd.DataFrame(final_sim)
    # fsim = (df[0],df[1],df[2]) 
    plot3D(simData, numDataPoints, FPS, filename, 3)      

    plt.show()
    plt.close()

main()
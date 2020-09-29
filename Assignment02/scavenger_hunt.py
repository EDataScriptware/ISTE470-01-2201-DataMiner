import matplotlib.pyplot as plt
import numpy as np

def read_waveforms(LA, RV, RA) :
    infile = open('waveforms.csv', 'r')

    line = infile.readline()
    wf = 0 # which waveform are we trying to read (0 = LA, 1 = RV, 2 = RA)
    
    while line :
        line = line.strip()
        data = line.split(',')

        for i in range(0, len(data)) : 
            data[i] = float(data[i])

        if(wf == 0) :
            LA.append(data)
        elif(wf == 1) :
            RV.append(data)
        elif(wf == 2) :
            RA.append(data)
        
        wf = (wf + 1) % 3
        line = infile.readline()

    infile.close()

def read_times(TL, TR) :
    infile = open('times.csv', 'r')
    line = infile.readline()
    data = line.strip().split(',')

    for i in range(0, len(data)) : 
        data[i] = float(data[i]) * MS

    TL.append(data)

    line = infile.readline()
    data = line.strip().split(',')

    for i in range(0, len(data)) : 
        data[i] = float(data[i]) * MS

    TR.append(data)
    infile.close()

def plot_waveforms(LA, RV, RA, TL, TR) :
    print('create your individual waveform plots here')

def reportStat(name,arr):
    return str(name + ": " +
    "min = " + str(np.amin(arr,axis=0)) +
    ", max = " + str(np.amax(arr,axis=0)) +
    ", avg = " + str(np.mean(arr,axis=0)))

def minimum(arr,xdi):
    return np.amin(arr,axis=xdi)
def average(arr,xdi):
    return np.mean(arr,axis=xdi)
def maximum(arr,xdi):
    return np.amax(arr,axis=xdi)

def find_nLargestValue(arr,n):
    unsorted5LV = np.sort(arr,axis=0)[-n:] # Grab top 5 largest values
    asc5LV = -np.sort(-unsorted5LV) # sort to Ascending
    return asc5LV

# make empty data and time Lists
LA_list = [] # LinearAcceleration
RV_list = [] # RotationalVelocity
RA_list = [] # RotationalAcceleration
TL_list = [] # TimeLinear
TR_list = [] # TimeRotational

# constants
MS = 1000

read_waveforms(LA_list, RV_list, RA_list)
read_times(TL_list, TR_list)

# convert all data and time lists to numpy arrays for plotting
LA = np.array(LA_list)
RV = np.array(RV_list)
RA = np.array(RA_list)
TL = np.array(TL_list[0])
TR = np.array(TR_list[0])

# data[i] = float(data[i]) * <conversion constant>

M_LA = minimum(LA,1)
print(reportStat('MLA',M_LA))
A_LA = average(LA,1)
print(reportStat('ALA',A_LA))
P_LA = maximum(LA,1)
print(reportStat('PLA',P_LA))
print("");
M_RV = minimum(RV,1)
print(reportStat('MRV',M_RV))
A_RV = average(RV,1)
print(reportStat('ARV',A_RV))
P_RV = maximum(RV,1)
print(reportStat('PRV',P_RV))
print("");
M_RA = minimum(RA,1)
print(reportStat('MRA',M_RA))
A_RA = average(RA,1)
print(reportStat('ARA',A_RA))
P_RA = maximum(RA,1)
print(reportStat('PRA',P_RA))
print("");

print("The largest values of PLA:\n" + 
        str(find_nLargestValue(P_LA,5)))
print("The largest values of PRV:\n" + 
        str(find_nLargestValue(P_RV,5)))
print("The largest values of PRA:\n" + 
        str(find_nLargestValue(P_RA,5)))
print("------------")

# Full Plot of A_LA, P_RV, P_RA
def displayFullPlot():
    sizP = np.pi * 4
    for i in range(0,1):
        
        plt.plot()
        plt.scatter(A_LA, P_RV,s=sizP,c='green',marker='.' ,label='ALA vs PRV')
        plt.scatter(A_LA, P_RA,s=sizP,c='blue',marker='.' ,label='ALA vs PRA')
        plt.scatter(P_RV,P_RA,s=sizP,c='orange',marker='.' ,label='PRV vs PRA')
        plt.legend()
        x_max = np.max(np.concatenate([A_LA,P_RV]))
        y_max = np.max(np.concatenate([P_RV,P_RA]))
        plt.xticks(np.arange(0,np.round(x_max,10)+10, step = 5))
        plt.yticks(np.arange(0,np.round(y_max,10)+10, step = 5))
        plt.title('Full Plot Overview')
        #plt.xlabel('Instances')
        #plt.ylabel('')

        #print(P_RV);
        #plt.savefig('Instance ' + str(i + 1) + '.png')
        plt.show()
        plt.close()


def displayThreeSlots():
    sizP = np.pi * 4
    for i in range(0, 1) :
        
        plt.figure(1)
        plt.plot()
        plt.scatter(A_LA, P_RV,s=sizP,c='green',marker='.',label='ALA vs PRV')
        plt.title('ALA vs PRV')
        x_max = np.max(A_LA)
        y_max = np.max(P_RV)
        plt.xticks(np.arange(0,np.round(x_max,10)+10, step = 5))
        plt.yticks(np.arange(0,np.round(y_max,10)+10, step = 5))
        #print("5 largest values " + str(find_nLargestValue(np.concatenate([A_LA,P_RV]),5)))

        plt.figure(2)
        plt.plot()
        plt.scatter(A_LA, P_RA,s=sizP,c='blue',marker='.',label='ALA vs PRA')
        plt.title('ALA vs PRA')
        x_max = np.max(A_LA)
        y_max = np.max(P_RV)
        plt.xticks(np.arange(0,np.round(x_max,10)+10, step = 5))
        plt.yticks(np.arange(0,np.round(y_max,10)+10, step = 5))

        plt.figure(3)
        plt.plot()
        plt.scatter(P_RV,P_RA,s=sizP,c='orange',marker='.',label='PRV vs PRA')
        plt.title('PRV vs PRA')
        x_max = np.max(P_RV)
        y_max = np.max(P_RA)
        plt.xticks(np.arange(0,np.round(x_max,10)+10, step = 5))
        plt.yticks(np.arange(0,np.round(y_max,10)+10, step = 5))
        
        #plt.savefig('Instance ' + str(i + 1) + '.png')
        plt.show()
        plt.close()

#displayFullPlot()
displayThreeSlots()
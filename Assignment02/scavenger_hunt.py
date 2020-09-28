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
        data[i] = float(data[i]) * 1000

    TL.append(data)

    line = infile.readline()
    data = line.strip().split(',')

    for i in range(0, len(data)) : 
        data[i] = float(data[i]) * 1000

    TR.append(data)
    infile.close()

def plot_waveforms(LA, RV, RA, TL, TR) :
    print('create your individual waveform plots here')


def maximum(arrayList):
    fullArray = []
    i = 0
    while i < len(arrayList):
        #print(i)
        j = 0
        while j < len(arrayList[i]):
            #print(arrayList[i][j])
            fullArray.append(arrayList[i][j])
            j = j + 1
        i = i + 1
    fullArray.sort()
    return str(fullArray[-1])



# make empty data and time Lists
LA_list = []
RV_list = []
RA_list = []
TL_list = []
TR_list = []



read_waveforms(LA_list, RV_list, RA_list)
read_times(TL_list, TR_list)


# convert all data and time lists to numpy arrays for plotting
LA = np.array(LA_list)
RV = np.array(RV_list)
RA = np.array(RA_list)
TL = np.array(TL_list[0])
TR = np.array(TR_list[0])

# print(""+ str(np.max(RV[0])))
def toString(string, array):
    print(string + " Min: " + str(np.min(array)) + " Max: " + str(np.max(array)) + " Average: " + str(np.average(array)))
# 
PRV = []
ARV = []
MRV = []

PLA = []
ALA = []
MLA = []

PRA = []
ARA = []
MRA = []

for i in RV:
    PRV.append(np.max(i))
    ARV.append(np.average(i))
    MRV.append(np.min(i))

for i in LA:
    PLA.append(np.max(i))
    ALA.append(np.average(i))
    MLA.append(np.min(i))

for i in RA:
    PRA.append(np.max(i))
    ARA.append(np.average(i))
    MRA.append(np.min(i))

toString("MLA", MLA)
toString("ALA", ALA)
toString("PLA", PLA)
print("\n")
toString("MRV", MRV)
toString("ARV", ARV)
toString("PRV", PRV)
print("\n")
toString("MRA", MRA)
toString("ARA", ARA)
toString("PRA", PRA)

area = np.pi*3
for i in range(0,1):
    plt.subplot(311)
    plt.scatter(PLA, PRA, s=area, color="black")
    plt.title('PLA vs PRA')
    plt.xlabel('PLA')
    plt.ylabel('PRA')
    plt.xticks(np.arange(0, 175, step=5))
    plt.yticks(np.arange(0, 65, step=5))


    # plt.subplot(312)
    # plt.plot(TR, RV[i, :], color="black")
    # plt.title('TR vs RV')
    # plt.xlabel('Time (ms)')
    # plt.ylabel('Rotational Velocity (rad/s)')
    # plt.xticks(np.arange(0, 56, step=7))

    # plt.subplot(313)
    # plt.plot(TR, RA[i, :], color="black")
    # plt.title('TR vs RA')
    # plt.xlabel('Time (ms)')
    # plt.ylabel('Rotational Velocity (rad/s^2)')
    # plt.xticks(np.arange(0, 56, step=7))

    




# for i in range(0, 1):
#     plt.subplot(311)
#     plt.plot(TL, LA[6, :], color='blue')
#     plt.title('TL vs LA')
#     plt.xlabel('Time (ms)')
#     plt.ylabel('Linear Accel (g)')
#     plt.xticks(np.arange(0, 55, step=5))


#     plt.subplot(312)
#     plt.plot(TR, RV[i, :], color='blue')
#     plt.title('TR vs RV')
#     plt.xlabel('Time (ms)')
#     plt.ylabel('Rotational Velocity (rad/s)')
#     plt.xticks(np.arange(0, 55, step=5))
    

#     plt.subplot(313)
#     plt.plot(TR, RA[i, :], color='blue')
#     plt.title('TR vs RA')
#     plt.xlabel('Time (ms)')
#     plt.ylabel('Rotational Accel (Rad/s^2)')
#     plt.xticks(np.arange(0, 55, step=5))

    
    plt.savefig('Instance' + str(i + 1) + '.png')
    plt.show()
    plt.close()















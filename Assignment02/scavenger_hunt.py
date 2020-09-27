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

print("PRV: Maximum: " + maximum(RV))
print("PRA: Maximum: " + maximum(RA))

# area = np.pi*3
# for i in range(0,1):
#     plt.subplot(311)
#     plt.scatter(TL, LA[6,:], s=area, color="black")
#     plt.title('TL vs LA')
#     plt.xlabel('Time (ms)')
#     plt.ylabel('Linear Accel (g)')
#     plt.xticks(np.arange(0, 56, step=7))

#     plt.subplot(312)
#     plt.scatter(TR, RV[i, :], s=area, color="black")
#     plt.title('TR vs RV')
#     plt.xlabel('Time (ms)')
#     plt.ylabel('Rotational Velocity (rad/s)')
#     plt.xticks(np.arange(0, 56, step=7))

#     plt.subplot(313)
#     plt.scatter(TR, RA[i, :], s=area, color="black")
#     plt.title('TR vs RA')
#     plt.xlabel('Time (ms)')
#     plt.ylabel('Rotational Velocity (rad/s^2)')
#     plt.xticks(np.arange(0, 56, step=7))

    




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

    
#     plt.savefig('Instance' + str(i + 1) + '.png')
#     plt.show()
#     plt.close()















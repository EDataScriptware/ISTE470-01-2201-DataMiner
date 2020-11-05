# Edward Riley

import sys, os, math

bigList = []

targetFile = str(sys.argv[1])

def read_arff(inputFile):
    bigList = []
    subList = []
    outputFlag = False
    with open(inputFile) as f:
        lines = f.readlines()
    counter = 0
    for line in lines:
        counter = counter + 1
        
        if outputFlag == True:
            subList = line.split(",")
            maximumSize = len(subList) - 1
            subList[maximumSize] = subList[maximumSize].replace("\n", "")
            bigList.append(subList)

        if line.strip() == "@data":
            outputFlag = True
    
    return bigList

bigList = read_arff(targetFile)

clusterZero  = []
clusterOne   = []
clusterTwo   = []
clusterThree = []
clusterFour  = []
clusterFive  = []
clusterSix   = []

for subList in bigList:
    sepalLength = float(subList[1])
    sepalWidth = float(subList[2])
    petalLength = float(subList[3])
    petalWidth = float(subList[4])
    clusterType = str(subList[5])

    sepal = (sepalLength, sepalWidth)
    petal = (petalLength, petalWidth)
    
    sepalPetalArray = [sepal, petal]

    if clusterType == "cluster0":
        clusterZero.append(sepalPetalArray)
    elif clusterType == "cluster1":
        clusterOne.append(sepalPetalArray)
    elif clusterType == "cluster2":
        clusterTwo.append(sepalPetalArray)
    elif clusterType == "cluster3":
        clusterThree.append(sepalPetalArray)
    elif clusterType == "cluster4":
        clusterFour.append(sepalPetalArray)
    elif clusterType == "cluster5":
        clusterFive.append(sepalPetalArray)
    elif clusterType == "cluster6":
        clusterSix.append(sepalPetalArray)
    else:
        print("ERROR WITH READING CLUSTER")
        sys.exit(-1)

    euclideanDistance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(sepal, petal)]))
    # print("Sepal: " + str(sepal) + "\nPetal: " + str(petal) + "\nEuclidean Distance: " + str(euclideanDistance) + "\n\n")

clusterList = []

if clusterZero:
    clusterList.append(clusterZero)

if clusterOne:
    clusterList.append(clusterOne)

if clusterTwo:
    clusterList.append(clusterTwo)

if clusterThree:
    clusterList.append(clusterThree)

if clusterFour:
    clusterList.append(clusterFour)

if clusterFive:
    clusterList.append(clusterFive)

if clusterSix:
    clusterList.append(clusterSix)

totalAverageDistanceArray = []

for clusterCategory in clusterList:
    totalDistance = 0
    counter = 0
    for pointXY in clusterCategory:
        currentSepalWidth = pointXY[0][0]
        currentSepalLength = pointXY[0][1]
        for pointValue in pointXY:

            counter += 1

        

            euclideanDistance = math.sqrt((currentSepalLength-currentSepalWidth)**2 + (pointXY[0][0]-pointXY[0][1])**2 )
            totalDistance += euclideanDistance
        #print(currentSepalLength)    
    totalAverageDistanceArray.append(totalDistance / counter)

    
        
print(totalAverageDistanceArray)
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

    #sepal = (sepalLength, sepalWidth)
    #petal = (petalLength, petalWidth)
    
    sepalPetalArray = [sepalLength, sepalWidth, petalLength, petalWidth]

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


# This is the correct formula. I (Edward) checked with Prof. Golen.

def calculateEulideanDistance(pOne, pTwo):
    euclideanDistance = math.sqrt(  (pOne[0]-pTwo[0])**2 + (pOne[1]-pTwo[1])**2 + (pOne[2]-pTwo[2])**2 + (pOne[3]-pTwo[3])**2 )
    return euclideanDistance

#firstPoint = clusterList[1][0]
#secondPoint = clusterList[1][1]

# print(firstPoint)
# print(secondPoint)

# result = calculateEulideanDistance(firstPoint, secondPoint)
# print(result)

# NOTES:
# >tricky
# function compute_coheison
# in compute_coheision, iterate across through all the clusters 
# for a given cluster, you iterate through all the points 
# for each point in the cluster, you need to calculate the distance to all points inside the cluster. (intra-cluster)
# Sum up all the distances then you divide by the number of points in the (lengthcluster - 1) 
# looks at cluster 1 and uses the first cluster to compare distances to other points.  (use the first point as a static variable)

# clusterList is a 2d array of clusters.
# clusterCategory is clusterZero, clusterOne, clusterTwo, etc. 

averageDistanceArray = []
totalDistance = 0
counter = 0
for clusterCategory in clusterList:
    try: 
        while True:
            counter += 1
            print(clusterCategory[0])
            print(clusterCategory[counter])
            
            totalDistance += calculateEulideanDistance(clusterCategory[0], clusterCategory[counter])

    except: 
        result = totalDistance / (counter - 1)
        averageDistanceArray.append(result)
        counter = 0
        totalDistance = 0


print(averageDistanceArray)

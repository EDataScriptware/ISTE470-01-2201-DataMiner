import sys
import os

# Checks to verify argument. 
totalSys = len(sys.argv)

if totalSys == 1:
    print("Missing input file and output file argument.")
    exit()
elif totalSys == 2:
    print("Missing output file argument.")
    exit()


inputFile = sys.argv[1]
outputFile = sys.argv[2]

def write_data(inputFile, outputFile, bigList, fileType):
    output = "@RELATION\tiris\n\n"
    output += "@ATTRIBUTE sepallength\tREAL\n"
    output += "@ATTRIBUTE sepalwidth\tREAL\n"
    output += "@ATTRIBUTE petallength\tREAL\n"
    output += "@ATTRIBUTE petalwidth\tREAL\n"
    output += "@ATTRIBUTE class\t{Iris-setosa,Iris-versicolor,Iris-virginica}\n"

    output += "\n@DATA\n"
    for subList in bigList:
        counter = 0
        for item in subList:
            counter = counter + 1
            if fileType == "csv":
                if counter is not 5:
                    output += (item + ",")
                else:
                        if int(item) is 1:
                            output += "Iris-setosa\n"
                        elif int(item) is 2:
                            output += "Iris-versicolor\n"
                        elif int(item) is 3:
                            output += "Iris-virginica\n"
                        else:
                            output += "none\n"
            else:
                if counter is not 5:
                    output += (item + ",")
                else:
                    output += (item + "\n")

    output = output[:-1]
    with open(outputFile, "w") as w:
        w.write(output)

def read_arff(inputFile, outputFile):
    bigList = []
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

        if line.strip() == "@DATA":
            outputFlag = True
        
    write_data(inputFile, outputFile, bigList, "arff")
            



# read_csv function
def read_csv(inputFile, outputFile):
    bigList = []
    with open(inputFile) as f:
        lines = f.readlines()
    for line in lines:
        subList = line.split(",")
        maximumSize = len(subList) - 1
        
        # Gets rid of \n in the last list item.
        subList[maximumSize] = subList[maximumSize].replace("\n", "")
        bigList.append(subList)
    write_data(inputFile, outputFile, bigList, "csv")
    

    
        

# Checks for file extension and redirects to the proper function. 
if inputFile.endswith(".csv"):
    read_csv(inputFile, outputFile)
elif inputFile.endswith(".arff"):
    read_arff(inputFile, outputFile)
else: 
    print("fail")


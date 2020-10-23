# Edward Riley

import sys
import os 

with open('games-features.arff') as f:
    lines = f.readlines()

chunk = ""
try: 
    i = 30 # MAKE SURE @data starts at line 31 AND the first data entry is at line 32 or this will not work!
    while True: 
        i = i + 1
        chunk = chunk + lines[i]
except:
    print("All data retrieved")

chunk = chunk.split("\n")

i = -1
dataList = []
try: 
    while True: 
        i = i + 1
        dataList.append(chunk[i].split(","))
except:
    print("All data separated")

output = ""

def yesOrNo(input):
    if str(input) == "0":
        return "no"
    else:
        return "yes"

with open('games-features_disc.arff', 'w') as f:
    i = -1

    output += "@RELATION games-disc\n"
    output += "@ATTRIBUTE recommendationCount {lower, low, medium, prehigh, high}\n"
    output += "@ATTRIBUTE Steamspyowners {lower, low, medium, prehigh, high}\n"
    output += "@ATTRIBUTE isFree {no, yes}\n"
    output += "@ATTRIBUTE categorySinglePlayer {no, yes}\n"
    output += "@ATTRIBUTE categoryMultiplayer {no, yes}\n"
    output += "@ATTRIBUTE categoryCoop {no, yes}\n"
    output += "@ATTRIBUTE categoryMMO {no, yes}\n"
    output += "@ATTRIBUTE categoryInAppPurchase {no, yes}\n"
    output += "@ATTRIBUTE categoryIncludesLevelEditor {no, yes}\n"
    output += "@ATTRIBUTE categoryVrSupport {no, yes}\n"
    output += "@ATTRIBUTE genreIsNongame {no, yes}\n"
    output += "@ATTRIBUTE genreIsIndie {no, yes}\n"
    output += "@ATTRIBUTE genreIsAction {no, yes}\n"
    output += "@ATTRIBUTE genreIsAdventure {no, yes}\n"
    output += "@ATTRIBUTE genreIsCasual {no, yes}\n"
    output += "@ATTRIBUTE genreIsStrategy {no, yes}\n"
    output += "@ATTRIBUTE genreIsRPG {no, yes}\n"
    output += "@ATTRIBUTE genreIsSimulation {no, yes}\n"
    output += "@ATTRIBUTE genreIsEarlyAccess {no, yes}\n"
    output += "@ATTRIBUTE genreIsFreeToPlay {no, yes}\n"
    output += "@ATTRIBUTE genreIsSports {no, yes}\n"
    output += "@ATTRIBUTE genreIsRacing {no, yes}\n"
    output += "@ATTRIBUTE genreIsMMO {no, yes}\n"
    output += "@ATTRIBUTE priceInitial {lower, low, medium, prehigh, high}\n"
    output += "@ATTRIBUTE priceHigh {lower, low, medium, prehigh, high}\n\n@DATA\n\n"
    
    try: 
        while True:
            i += 1

            # Recommendation Count
            if int(dataList[i][2]) < 1000:
                output += "lower,"
            elif  1000 <= int(dataList[i][3]) and int(dataList[i][3]) < 3000:
                output += "low,"
            elif 3000 <= int(dataList[i][3]) and int(dataList[i][3]) < 10000:
                output += "medium,"
            elif 10000 <= int(dataList[i][3]) and int(dataList[i][3]) < 50000:
                output += "prehigh,"
            else:
                output += "high,"

            # Steamspyowners
            if int(dataList[i][3]) < 5000:
                output += "lower,"
            elif  5000 <= int(dataList[i][3]) and int(dataList[i][3]) < 10000:
                output += "low,"
            elif 10000 <= int(dataList[i][3]) and int(dataList[i][3]) < 25000:
                output += "medium,"
            elif 25000 <= int(dataList[i][3]) and int(dataList[i][3]) < 1000000:
                output += "prehigh,"
            else:
                output += "high,"

            # Is Free?
            output += str(yesOrNo(dataList[i][4]) + ",")

            # CategorySinglePlayer?
            output += yesOrNo(dataList[i][5]) + ","
        
            # CategoryMultiplayer?
            output += yesOrNo(dataList[i][6]) + ","

            # CategoryCoop?
            output += yesOrNo(dataList[i][7]) + ","

            # CategoryMMO?
            output += yesOrNo(dataList[i][8]) + ","

            # CategoryInAppPurchase?
            output += yesOrNo(dataList[i][9])  + ","

            # CategoryIncludesLevelEditor?
            output += yesOrNo(dataList[i][10]) + ","

            # categoryVrSupport
            output += yesOrNo(dataList[i][11]) + ","

            # genreIsNongame
            output += yesOrNo(dataList[i][12]) + ","

            # genreIsAction
            output += yesOrNo(dataList[i][13]) + ","

            # genreIsAdventure
            output += yesOrNo(dataList[i][14]) + ","

            # genreIsCasual
            output += yesOrNo(dataList[i][15]) + ","

            # genreIsStrategy
            output += yesOrNo(dataList[i][16]) + ","

            # genreIsRPG            
            output += yesOrNo(dataList[i][17]) + ","
            
            # genreIsSimulation 
            output += yesOrNo(dataList[i][18]) + ","

            # genreIsEarlyAccess
            output += yesOrNo(dataList[i][19]) + ","

            # genreIsFreeToPlay
            output += yesOrNo(dataList[i][20]) + ","

            # genreIsSports
            output += yesOrNo(dataList[i][21]) + ","

            # genreIsRacing
            output += yesOrNo(dataList[i][22]) + ","

            # genreIsMMO
            output += yesOrNo(dataList[i][23]) + ","

            output += yesOrNo(dataList[i][24]) + ","


            if float(dataList[i][25]) < 4.99:
                output += "lower,"
            elif  4.99 <= float(dataList[i][25]) and float(dataList[i][25]) < 9.99:
                output += "low,"
            elif 9.99 <= float(dataList[i][25]) and float(dataList[i][25]) < 19.99:
                output += "medium,"
            elif 19.99 <= float(dataList[i][25]) and float(dataList[i][25]) < 49.99:
                output += "prehigh,"
            else:
                output += "high,"

            if float(dataList[i][26]) < 4.99:
                output += "lower"
            elif  4.99 <= float(dataList[i][26]) and float(dataList[i][26]) < 9.99:
                output += "low"
            elif 9.99 <= float(dataList[i][26]) and float(dataList[i][26]) < 19.99:
                output += "medium"
            elif 19.99 <= float(dataList[i][26]) and float(dataList[i][26]) < 49.99:
                output += "prehigh"
            else:
                output += "high"

            output += "\n"


    except Exception as e: 
        print("Compiled!: " + str(e))
    f.write(output)

        

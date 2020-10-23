# Edward Riley

import sys
import os

subList = ""
bigList = []
subList = []

output = ""

with open("games-features.csv") as f:
    lines = f.readlines()
    for line in lines:
        subList = line.split(",")

        maximumSize = len(subList) - 1
        subList[maximumSize] = subList[maximumSize].replace("\r\n", "")

        bigList.append(subList)
        

        
        # Gets rid of \n in the last list item.


with open("games-features.arff", "w") as f:
    output =  "@RELATION games\n"                       
    output += "@ATTRIBUTE queryID\tstring\n"
    output += "@ATTRIBUTE queryName\tstring\n"
    output += "@ATTRIBUTE recommendationCount\treal\n"
    output += "@ATTRIBUTE Steamspyowners\treal\n"
    output += "@ATTRIBUTE isFree\treal\n"
    output += "@ATTRIBUTE categorySinglePlayer\treal\n"
    output += "@ATTRIBUTE categoryMultiplayer\treal\n"
    output += "@ATTRIBUTE categoryCoop\treal\n"
    output += "@ATTRIBUTE categoryMMO\treal\n"
    output += "@ATTRIBUTE categoryInAppPurchase\treal\n"
    output += "@ATTRIBUTE categoryIncludesLevelEditor\treal\n"
    output += "@ATTRIBUTE categoryVrSupport\treal\n"
    output += "@ATTRIBUTE genreIsNongame\treal\n"
    output += "@ATTRIBUTE genreIsIndie\treal\n"
    output += "@ATTRIBUTE genreIsAction\treal\n"
    output += "@ATTRIBUTE genreIsAdventure\treal\n"
    output += "@ATTRIBUTE genreIsCasual\treal\n"
    output += "@ATTRIBUTE genreIsStrategy\treal\n"
    output += "@ATTRIBUTE genreIsRPG\treal\n"
    output += "@ATTRIBUTE genreIsSimulation\treal\n"
    output += "@ATTRIBUTE genreIsEarlyAccess\treal\n"
    output += "@ATTRIBUTE genreIsFreeToPlay\treal\n"
    output += "@ATTRIBUTE genreIsSports\treal\n"
    output += "@ATTRIBUTE genreIsRacing\treal\n"
    output += "@ATTRIBUTE genreIsMMO\treal\n"
    output += "@ATTRIBUTE priceInitial\treal\n"
    output += "@ATTRIBUTE priceFinal\treal\n"
    
    output += "\n\n@DATA\n\n"

    def booleanConverterSubList(row):
        if row == "True":
            return "1"
        elif row == "False":
            return "0"
        else:
            return "N/A"
        
    count = 0

    for subList in bigList:
            count += 1
            if count == 1:
                variable = "do nothing";
            else:
                output += subList[0] + ","                                  # QueryID
                queryName = subList[2].replace(" ", "-")                                # QueryName
                queryName = queryName.replace("'", "") + ","
                output += queryName
                output += subList[12] + ","                                 # RecommendationCount
                output += subList[15] + ","                                 # SteamSpyOwners
                output += str(booleanConverterSubList(subList[22])) + ","   # isFree
                output += str(booleanConverterSubList(subList[35])) + ","   # CategorySinglePlayer
                output += str(booleanConverterSubList(subList[36])) + ","   # CategoryMultiplayer
                output += str(booleanConverterSubList(subList[37])) + ","   # CategoryCoop
                output += str(booleanConverterSubList(subList[38])) + ","   # CategoryMMO
                output += str(booleanConverterSubList(subList[39])) + ","   # CategoryInAppPurchases
                output += str(booleanConverterSubList(subList[41])) + ","   # CategoryIncludesLevelEditor
                output += str(booleanConverterSubList(subList[42])) + ","   # CategoryVRSupport
                output += str(booleanConverterSubList(subList[43])) + ","   # GenreIsNongame
                output += str(booleanConverterSubList(subList[44])) + ","   # GenreIsIndie
                output += str(booleanConverterSubList(subList[45])) + ","   # GenreIsAction
                output += str(booleanConverterSubList(subList[46])) + ","   # GenreIsAdventure
                output += str(booleanConverterSubList(subList[47])) + ","   # GenreIsCasual
                output += str(booleanConverterSubList(subList[48])) + ","   # GenreIsStrategy
                output += str(booleanConverterSubList(subList[49])) + ","   # GenreIsRPG
                output += str(booleanConverterSubList(subList[50])) + ","   # GenreIsSimulation
                output += str(booleanConverterSubList(subList[51])) + ","   # GenreIsEarlyAccess
                output += str(booleanConverterSubList(subList[52])) + ","   # GenreIsFreeToPlay
                output += str(booleanConverterSubList(subList[53])) + ","   # GenreIsSports
                output += str(booleanConverterSubList(subList[54])) + ","   # GenreIsRacing
                output += str(booleanConverterSubList(subList[55])) + ","   # GenreIsMMO
                output += subList[57] + ","                                 # PriceInitial
                output += (subList[58]) + ""                               # PriceFinal




                output += "\n"
    f.write(output)


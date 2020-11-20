# Edward Riley & Vincent Venutolo

import sys
import os
import chardet as cd

subList = ""
bigList = []
subList = []
headers = []
output = ""

i = 0
with open("games-features.csv", encoding="utf-8", errors="replace") as f:
    lines = f.readlines()
    for line in lines:
        if i == 0:
            headers = line.split(",")
        i += 1
        subList = line.split(",")
        maximumSize = len(subList) - 1
        subList[maximumSize] = subList[maximumSize].replace("\r\n", "")

        bigList.append(subList)

        # Gets rid of \n in the last list item.

def listHeaders():
        cnt = 0
        for h in headers:
            print(str(cnt)+" = "+h)
            cnt += 1

with open("games-features.arff", "w", encoding="utf-8", errors="replace") as f:
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



    # Custom Error Exception
    class RecordHasEmptyField(Exception):
        """Record has one of emptied fields. So, It cannot be added to arff file."""


    for subList in bigList:
        count += 1
        if count == 1:
            variable = "do nothing";
        else:
            try:
                if any(x == '' for x in subList):
                    raise RecordHasEmptyField(count)

                record = ""
                record += subList[0] + ","                                  # QueryID
                queryName = subList[2].replace(" ", "-")                    # QueryName
                queryName = queryName.replace("'", "") + ","
                record += queryName
                record += subList[12] + ","                                 # RecommendationCount
                record += subList[15] + ","                                 # SteamSpyOwners
                record += str(booleanConverterSubList(subList[22])) + ","   # isFree
                record += str(booleanConverterSubList(subList[35])) + ","   # CategorySinglePlayer
                record += str(booleanConverterSubList(subList[36])) + ","   # CategoryMultiplayer
                record += str(booleanConverterSubList(subList[37])) + ","   # CategoryCoop
                record += str(booleanConverterSubList(subList[38])) + ","   # CategoryMMO
                record += str(booleanConverterSubList(subList[39])) + ","   # CategoryInAppPurchases
                record += str(booleanConverterSubList(subList[41])) + ","   # CategoryIncludesLevelEditor
                record += str(booleanConverterSubList(subList[42])) + ","   # CategoryVRSupport
                record += str(booleanConverterSubList(subList[43])) + ","   # GenreIsNongame
                record += str(booleanConverterSubList(subList[44])) + ","   # GenreIsIndie
                record += str(booleanConverterSubList(subList[45])) + ","   # GenreIsAction
                record += str(booleanConverterSubList(subList[46])) + ","   # GenreIsAdventure
                record += str(booleanConverterSubList(subList[47])) + ","   # GenreIsCasual
                record += str(booleanConverterSubList(subList[48])) + ","   # GenreIsStrategy
                record += str(booleanConverterSubList(subList[49])) + ","   # GenreIsRPG
                record += str(booleanConverterSubList(subList[50])) + ","   # GenreIsSimulation
                record += str(booleanConverterSubList(subList[51])) + ","   # GenreIsEarlyAccess
                record += str(booleanConverterSubList(subList[52])) + ","   # GenreIsFreeToPlay
                record += str(booleanConverterSubList(subList[53])) + ","   # GenreIsSports
                record += str(booleanConverterSubList(subList[54])) + ","   # GenreIsRacing
                record += str(booleanConverterSubList(subList[55])) + ","   # GenreIsMMO
                record += subList[57] + ","                                 # PriceInitial
                record += (subList[58]) + ""                               # PriceFinal

                output += record
            except RecordHasEmptyField as re:
                # Skipping this to next iteration
                print('Cannot add #'+str(count)+' Record because it contains an empty field.')
                continue

        output += "\n"

    f.write(output)
    
listHeaders()
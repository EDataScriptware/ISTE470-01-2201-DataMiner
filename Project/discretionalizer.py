# Edward Riley & Vincent Venutolo

import sys
import os

dataList = []
headers = []
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

        dataList.append(subList)
output = ""

# Custom Error Exception
class RecordHasEmptyField(Exception):
    """Record has one of emptied fields. So, It cannot be added to arff file."""

def listHeaders():
        cnt = 0
        for h in headers:
            print(str(cnt) + " = " + str(h))
            cnt += 1

def isFloat(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

def isInt(input):
    try:
        int(float(input))
        return True
    except ValueError:
        return False

def yesOrNo(input,cnt):
    s = str(input)
    if s == "0" or s == "False":
        return "yes"
    elif s == '1' or s == "True":
        return "no"
    else:
        raise RecordHasEmptyField(cnt)

def checkErrorTypes(input, cnt):
    if input == None and (type(input) == str and input == "USB"):
        raise RecordHasEmptyField(cnt)
output = ""

with open('games-features_disc.arff', 'w', encoding="utf-8", errors="replace") as f:

    output += "@RELATION games-disc\n"
    output += "@ATTRIBUTE recommendationCount {lower, low, medium, prehigh, high}\n"
    output += "@ATTRIBUTE numberOfOwners {lower, low, medium, prehigh, high}\n"
    output += "@ATTRIBUTE isFree {no, yes}\n" #1
    output += "@ATTRIBUTE categorySinglePlayer {no, yes}\n" #2
    output += "@ATTRIBUTE categoryMultiplayer {no, yes}\n" #3
    output += "@ATTRIBUTE categoryCoop {no, yes}\n" #4
    output += "@ATTRIBUTE categoryMMO {no, yes}\n" #5
    output += "@ATTRIBUTE categoryInAppPurchase {no, yes}\n" #6
    output += "@ATTRIBUTE categoryIncludesLevelEditor {no, yes}\n" #7
    output += "@ATTRIBUTE categoryVrSupport {no, yes}\n" #8
    output += "@ATTRIBUTE genreIsNongame {no, yes}\n"#9
    output += "@ATTRIBUTE genreIsIndie {no, yes}\n"#10
    output += "@ATTRIBUTE genreIsAction {no, yes}\n" #11
    output += "@ATTRIBUTE genreIsAdventure {no, yes}\n" #12
    output += "@ATTRIBUTE genreIsCasual {no, yes}\n" #13
    output += "@ATTRIBUTE genreIsStrategy {no, yes}\n" #14
    output += "@ATTRIBUTE genreIsRPG {no, yes}\n" #15 
    output += "@ATTRIBUTE genreIsSimulation {no, yes}\n" #16
    output += "@ATTRIBUTE genreIsEarlyAccess {no, yes}\n" #17
    output += "@ATTRIBUTE genreIsFreeToPlay {no, yes}\n" #18
    output += "@ATTRIBUTE genreIsSports {no, yes}\n" #19
    output += "@ATTRIBUTE genreIsRacing {no, yes}\n" #20
    output += "@ATTRIBUTE genreIsMMO {no, yes}\n" #21
    output += "@ATTRIBUTE priceInitial {Below_$4.99, $4.99-$9.98, $9.99-$19.99, $20-$49.99, Above_$50}\n"
    output += "@ATTRIBUTE priceFinal {Below_$4.99, $4.99-$9.98, $9.99-$19.99, $20-$49.99, Above_$50}\n\n\n@DATA\n\n\n"
# should be one worded attribute
    listRecordWithErrors = []
    count = 0
    for data in dataList:
        count += 1
        try:
            record = ''
            
            if not isInt(data[12]) or not isInt(data[13]):
                raise RecordHasEmptyField(count)

            # Recommendation Count
            checkErrorTypes(data[12],count)

            if int(data[12]) < 1000:
                record += "lower,"
            elif  1000 <= int(data[12]) and int(data[12]) < 3000:
                record += "low,"
            elif 3000 <= int(data[12]) and int(data[12]) < 10000:
                record += "medium,"
            elif 10000 <= int(data[12]) and int(data[12]) < 50000:
                record += "prehigh,"
            else:
                record += "high,"
            
            # Steamspyowners
            checkErrorTypes(data[15],count)
            if int(data[15]) < 5000:
                record += "lower,"
            elif  5000 <= int(data[15]) and int(data[15]) < 10000:
                record += "low,"
            elif 10000 <= int(data[15]) and int(data[15]) < 25000:
                record += "medium,"
            elif 25000 <= int(data[15]) and int(data[15]) < 1000000:
                record += "prehigh,"
            else:
                record += "high,"
            

            # Dicrete all selected attributes
            h = 22
            while h < len(headers):
                if (not h >= 23 and h <= 34) or (h >= 35 and h <= 55) and h != 40:
                    #print(str(h) + ' ' + data[h])
                    rd = ''
                    rd = str(yesOrNo(data[h],count) + ",")
                    record += rd
                h += 1

            # PriceInitial
            checkErrorTypes(data[57],count)
            tdata = []
            if (str(data[57]) == 'False' or str(data[57]) == 'True') and (str(data[58]) == 'USD' or (str(data[58]) == '' or len(str(data[58])) > 0)):
                tdata.append(data[59])
                tdata.append(data[60])
            elif (str(data[57]) == 'USD' and isFloat(data[58])) or ((str(data[57]) == '' or str(data[57]) == ' ') and isFloat(data[58])):
                tdata.append(data[58])
                tdata.append(data[59])
            else:
                tdata.append(data[57])
                tdata.append(data[58])
            
            checkErrorTypes(tdata[0],count)
            if float(tdata[0]) < 4.99:
                record += "Below_$4.99,"
            elif  4.99 <= float(tdata[0]) and float(tdata[0]) < 9.99:
                record += "$4.99-$9.98,"
            elif 9.99 <= float(tdata[0]) and float(tdata[0]) < 19.99:
                record += "$9.99-$19.99,"
            elif 19.99 <= float(tdata[0]) and float(tdata[0]) < 49.99:
                record += "$20-$49.99,"
            else:
                record += "Above_$50,"

            # PriceHigh
            checkErrorTypes(tdata[1],count)
            if float(tdata[1]) < 4.99:
                record += "Below_$4.99"
            elif  4.99 <= float(tdata[1]) and float(tdata[1]) < 9.99:
                record += "$4.99-$9.98"
            elif 9.99 <= float(tdata[1]) and float(tdata[1]) < 19.99:
                record += "$9.99-$19.99"
            elif 19.99 <= float(tdata[1]) and float(tdata[1]) < 49.99:
                record += "$20-$49.99"
            else:
                record += "Above_$50"
            
            record += "\n"
            output += record
        except RecordHasEmptyField as re:
            # Skipping this to next iteration
            print('Cannot add #' + str(count) + ' Record because it contains an empty field.')
            listRecordWithErrors.append('#' + str(count) + ' Record has empty field.')
            continue
        except ValueError as ve:
            print(ve)
            print(' #' + str(count) + ' = ' + str(data[57]) + ' OR ' + str(data[58]))
            listRecordWithErrors.append('#' + str(count) + ' = ' + str(data[57]) + ' OR ' + str(data[58]))
            continue
        except Exception as e: 
            print(e)
            print(str(count) + " Records Compiled!")
            break
    print("Total of Flawed Records: ",len(listRecordWithErrors))
    
    f.write(output)
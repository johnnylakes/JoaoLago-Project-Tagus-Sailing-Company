from Skipper import *
from SkipperCollection import *


  def tieBreaker(PM):
    if len(PM) == 0:
        return "Not-assigned"
    for i in range(len(PM)):
        if len(PM) == 1:
            return PM[0]
        for j in range(i+1,len(PM)):
            sk_escolhido = PM[i]
            if sk_escolhido.getprice() > PM[j].getprice():
                sk_escolhido = PM[j]
            elif sk_escolhido.getprice() == PM[j].getprice():
                if int(sk_escolhido.getaccH()) > int(PM[j].getaccH()):
                    sk_escolhido = PM[j]
                elif sk_escolhido.getaccH() == PM[j].getaccH():
                    if sk_escolhido.getName() > PM[j].getName():
                        sk_escolhido = PM[j]

    return sk_escolhido
                




def findMatchingSkipper(req,skipcol):
    possibleMatch = []
    for skip in skipcol:
        date_hour = skip.getdata()
        dateList = date_hour.replace("(","").replace(")","").split(' ')
        if isIntersect(req.getLang(),skip.getlang())\
            and checkEquals(req.getCat(),skip.getcat())\
                and checkEquals(req.getType(),skip.gettype()) \
                    and int(skip.getaccH()) + int(req.getNumbH()) <= int(skip.getTmax())\
                        and int(req.getNumbH()) + hourToInt(dateList[1]) <= 20:
            possibleMatch.append(skip)

    sk_escolhido = tieBreaker(possibleMatch)
    if type(sk_escolhido) != str:
        sk_escolhido.setaccH(int(sk_escolhido.getaccH()) + int(req.getNumbH()))
        dateUpdate(sk_escolhido,req.getNumbH())
        
    #print(sk_escolhido)      
    return sk_escolhido

def dateUpdate(skipper,reqhour):
    reqhour = int(reqhour)
    date_hour = skipper.getdata()
    date_hour = date_hour[1:]
    #print(date_hour)
    dateList = date_hour.replace("(","").replace(")","").split(' ')
    #print(dateList)
    minutes = minutesToInt(dateList[1])
    hour = hourToInt(dateList[1])
    date = dateList[0]
    #print(date)
    day = dayToInt(date)
    month = monthToInt(date)
    year = yearToInt(date)
    if minutes == 0:
        if hour + reqhour < 20:
            hour+=reqhour
        else:
            hour = 8
            if day < 30:
                day+=1
            else:
                day = 1
                if month < 12:
                    month += 1
                else:
                    month = 1
                    year += 1
    else:
        if hour + reqhour < 19:
            hour+=reqhour
        else:
            hour = 8
            if day < 30:
                day+=1
            else:
                day = 1
                if month < 12:
                    month += 1
                else:
                    month = 1
                    year += 1
    timeToString = intToTime(hour,minutes)
    dateToString = intToDate(day,month,year)
    skipper.setdata("(" + dateToString + " " + timeToString + ")")
    #print(skipper.getdata())




reqCol = requestCollection()
reqCol.createCollection("projeto/testSets_v1/testSet4/requests13h00.txt")

col = skipperCollection()
col.createCollection("projeto/testSets_v1/testSet4/skippers13h00.txt")

sch = schedule()
sch.matchCol(col,reqCol)



#sch.displayCol()


skip_Infile = open("projeto/testSets_v1/testSet4/skippers13h00.txt","r")
skList = skip_Infile.readlines()
myfileString = "projeto/testSets_v1/testSet4/skippers13h00.txt"
date = skList[3]
time = skList[5]
NewfilenameSkip = createFileName("projeto/testSets_v1/testSet4/skippers13h00.txt",time)
timeList = UpdateFileTime(date,time)
skip_outfile = open(NewfilenameSkip, "w")
header = createHeader(NewfilenameSkip,timeList[0],timeList[1])
for lines in header:
    skip_outfile.write(lines + "\n")
for skip in col.getCollection():
    skip_outfile.write(skip.__str__() + "\n")

skip_outfile.close()



sch_Infile = open("projeto/testSets_v1/testSet4/schedule13h00.txt","r")
schList = sch_Infile.readlines()
oldschList, date, time = checkIfSchStay("projeto/testSets_v1/testSet4/schedule13h00.txt")
NewfilenameSch = createFileName("projeto/testSets_v1/testSet4/schedule13h00.txt",time)
timeList = UpdateFileTime(date,time)
sch_outfile = open(NewfilenameSch, "w")
headerSch = createHeader(NewfilenameSch,timeList[0],timeList[1])
for lines in headerSch:
    sch_outfile.write(lines + "\n")


writeList = sch.__str__()
#print(writeList)
outList = oldschList + writeList

outList = sortList(outList,date.replace("\n",""))



#Fazer o sort das listas, fazer um try except quando o ficheiro não tem o nome correto, passar as funções tie breaker para a classe schedule
#print(outList)

#print(writeList)
#Sorter(writeList)
#print(writeList)

for line in outList:
    sch_outfile.writelines(line + "\n")

sch_outfile.close()





#skip_outfile = open("projeto/testSets_v1/testSet1/skippers17h00.txt","w")
#header = ["Company:","Tagus Sailing","Day:",,"Time:",time,"Skippers:"]
#for lines in header:
#    skip_outfile.write(lines)

#line = []
#for skip in col:

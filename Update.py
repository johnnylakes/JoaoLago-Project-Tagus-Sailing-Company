from auxy import *
from RequestCollection import RequestCollection
from SkipperCollection import SkipperCollection
from Schedule import Schedule
import sys

def update(skipperFile,scheduleFile,requestFile):
    '''
        Create two updated text files from three files, request file, skipper file, schedule.
        The two files created are updated versios os the skipper files and the schedule file given.

        Requires:
        Three files, skipper text file, schedule text file and a request text file.

        Ensures:
        Return two text file corresponding to updating versios os the skipper file and schedule file.
    '''

    reqCol = RequestCollection()
    reqCol.createCollection(requestFile)

    col = SkipperCollection()
    col.createCollection(skipperFile)

    sch = Schedule()
    sch.matchCol(col,reqCol)

    skip_Infile = open(skipperFile,"r")
    skList = skip_Infile.readlines()
    date = skList[3]
    time = checkFileError(skipperFile)
    NewfilenameSkip = createFileName(skipperFile,time)
    timeList = UpdateFileTime(date,time)
    skip_outfile = open(NewfilenameSkip, "w")
    header = createHeader(NewfilenameSkip,timeList[0],timeList[1])
    for lines in header:
        skip_outfile.write(lines + "\n")
    for skip in col.getCollection():
        skip_outfile.write(skip.__str__() + "\n")
    skip_outfile.close()


    sch_Infile = open(scheduleFile,"r")
    schList = sch_Infile.readlines()
    time = checkFileError(scheduleFile)
    oldschList, date = checkIfSchStay(scheduleFile)
    #time = checkFileError(scheduleFile)
    NewfilenameSch = createFileName(scheduleFile,time)
    timeList = UpdateFileTime(date,time)
    sch_outfile = open(NewfilenameSch, "w")
    headerSch = createHeader(NewfilenameSch,timeList[0],timeList[1])
    for lines in headerSch:
        sch_outfile.write(lines + "\n")

    writeList = sch.__str__()
    outList = oldschList + writeList
    outList = sortList(outList,date.replace("\n",""))
    for line in outList:
        sch_outfile.writelines(line + "\n")

    sch_outfile.close()

    return sch_outfile,skip_outfile

update("testSets_v1/testSet3/skippers10h00.txt","testSets_v1/testSet3/schedule10h00.txt","testSets_v1/testSet3/requests10h00.txt")

#update(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]))

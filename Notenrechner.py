import csv
import sys
import getopt


def printMarks(marks):
    for element in marks:
        print("Fach: " + str(element[0]) + " | LP: " +
              str(int(element[1])) + " | Note: " + str(element[2]))


def sortByThirdElement(val):
    return val[2]


def main(argv):
    lpThreshold = 90
    try:
        opts, args = getopt.getopt(argv, "t:a")
    except getopt.GetoptError:
        print("Failed")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-a':
            print("A found") 
            lpThreshold = sys.float_info.max
        elif opt == '-t':
            print("t Found, t=" + arg)
            lpThreshold = float(arg)
      
    with open('noten.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')
        marks = []
        print("Reading marks...")
        for row in csv_reader:
            marks.append((row[0], row[1], row[2]))
        
        print("Sorting marks...")
        marks.sort(key=sortByThirdElement)
        printMarks(marks)

        print("Calculating average mark...")
        lpCount = 0
        markSum = 0.0
        listOfUsedSubjects = []
        for mark in marks:
            if(lpCount >= lpThreshold):
                break
            if((lpCount + float(mark[1])) <= lpThreshold):
                markSum += (float(mark[2]) * float(mark[1]))
                listOfUsedSubjects.append((mark[0], mark[1], mark[2]))
                lpCount += float(mark[1])
            else:
                markSum += (float(mark[2]) * float(lpThreshold - lpCount))
                listOfUsedSubjects.append((mark[0], (lpThreshold - lpCount), mark[2]))
                lpCount = lpThreshold
        printMarks(listOfUsedSubjects)
        print("Average mark: " + str((markSum / lpCount)))


if __name__ == "__main__":
   main(sys.argv[1:])

# attempt to make a script for making up for my poor decisions 
# Converts a newline separated list of statements into a github 
# markdown table following the format for CMPUT 301 

import sys

# constants for left column of the table, in order they should appear 
tableCategories = ("Use Case Name", "Covers User Stories", "Participating Actors", "Goal", "Trigger", 
                "Precondition", "Postcondition", "Basic Flow", "Exceptions", "Notes")
   

class TableDict: 
    tableDict = dict()

    def __init__(self):
        for x in tableCategories:
            self.tableDict[x] = ""

    def setRowVal(self, key, val):
        self.tableDict[key] = val

    def makeRow(self, left, right):
        return "| " + left + " | " + right + " |"

    def fixUseCaseName(self):
        oldName = self.tableDict.get(tableCategories[0])
        wordList = oldName.split(" ")
        newName = ""
        for w in wordList: 
            newName += w.capitalize()

        self.tableDict[tableCategories[0]] = newName

    def makeTable(self):
        tableString = ""

        # make title row first
        self.fixUseCaseName()
        tableString += self.makeRow(tableCategories[0], self.tableDict.get(tableCategories[0])) + "\n"
        tableString += "| --- | --- |\n"
        for i in range (1, len(tableCategories)):
            tableString += self.makeRow(tableCategories[i], self.tableDict.get(tableCategories[i])) + "\n"

        return tableString


def parseFileString(str):
    lineList = str.split("\n")
    rows = TableDict()

    tempCurrentKey = ""
    tempCurrentVal = ""

    for l in lineList:
        if l in tableCategories:
            rows.setRowVal(tempCurrentKey, tempCurrentVal)
            tempCurrentKey = l
            tempCurrentVal = ""
        else:
            if tempCurrentVal == "":
                tempCurrentVal = l
            else:
                tempCurrentVal = tempCurrentVal + "<br> " + l

    # set last
    rows.setRowVal(tempCurrentKey, tempCurrentVal)
               
    return rows

if __name__ == "__main__":
    # print ('Number of arguments:', len(sys.argv), 'arguments.')
    # print ('Argument List:', str(sys.argv))
    inputfile = None
    outputfile = None 
    outputString = ""

    if (len(sys.argv) < 2 or len(sys.argv) > 3):
        print("Invalid use, run as: \n \
            python " + sys.argv[0] + " [filename] [optional output file]\n")
        sys.exit(0)
    
    # good arguments 
    inputfile = sys.argv[1]
    if len(sys.argv) == 3: 
        outputfile = sys.argv[2]

    inFileFd = open(inputfile, "r")

    inputString = inFileFd.read()
    inFileFd.close()
    # print(inputString)
    outputString = parseFileString(inputString).makeTable()

    if not (outputfile is None):
        outFileFd = open(outputfile,"w+")
        outFileFd.write(outputString)
        outFileFd.close()
    else:
        print(outputString)


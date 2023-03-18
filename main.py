import sys
import csv

# This function use Needleman-Wunsch Algorithm to implement global sequence alignment


# Sequence1 is represented by columns & sequence2 is represented by rows
def Needleman(sequence1, sequence2):
    # rowLength is the total amount of columns & columnLength is the total amount of rows
    rowLength = len(sequence1)
    columnLength = len(sequence2)

    # Initializing the matrix and ScoringMatrix to 0
    matrix = [[0 for rows in range(rowLength+1)] for columns in range(columnLength+1)]
    scoringMatrix = [[0 for rows in range(rowLength)] for columns in range(columnLength)]

    # initialization step
    # F_0,j = d * j & F_i,0 = d * i, where 'd' is the gap penalty

    d = -2

    for row in range(columnLength + 1):
        matrix[row][0] = d * row

    for column in range(rowLength+1):
        matrix[0][column] = d * column

    # Calculating Scoring Matrix
    for row in range(columnLength):
        for column in range(rowLength):
            if sequence1[column] == sequence2[row]:
                scoringMatrix[row][column] = 1
            else:
                scoringMatrix[row][column] = -1

    # Calculating max of F_i,j
    for row in range(1, columnLength + 1):
        for column in range(1, rowLength + 1):
            prevDiagonal = matrix[row - 1][column - 1] + scoringMatrix[row-1][column-1]
            prevColumn = matrix[row][column-1] + d
            prevRow = matrix[row-1][column] + d

            matrix[row][column] = max(prevDiagonal, prevColumn, prevRow)

    # Tracing the route

    # sequenceAligned1 represent the second word and sequenceAligned2 represent the first word
    sequenceAligned1 = ""
    sequenceAligned2 = ""

    iTrace = columnLength
    jTrace = rowLength

    while iTrace >= 0 and jTrace > 0 or iTrace > 0 and jTrace >= 0:
        if iTrace > 0 and matrix[iTrace][jTrace] == matrix[iTrace-1][jTrace] + d:
            sequenceAligned1 = sequence2[iTrace - 1] + sequenceAligned1
            sequenceAligned2 = "-" + sequenceAligned2

            iTrace -= 1
        elif jTrace > 0 and matrix[iTrace][jTrace] == matrix[iTrace][jTrace-1] + d:
            sequenceAligned1 = "-" + sequenceAligned1
            sequenceAligned2 = sequence1[jTrace - 1] + sequenceAligned2

            jTrace -= 1
        else:
            sequenceAligned1 = sequence2[iTrace - 1] + sequenceAligned1
            sequenceAligned2 = sequence1[jTrace - 1] + sequenceAligned2

            iTrace -= 1
            jTrace -= 1

    print(sequenceAligned2 + " " + sequenceAligned1 + " " + str(matrix[columnLength][rowLength]))


if len(sys.argv) > 1:
    inputList = []
    with open(sys.argv[1], 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        next(csvReader)
        for line in csvReader:
            inputList.append(line)

    count = 0
    while count < len(inputList):
        Needleman(inputList[count][0], inputList[count][1])
        count += 1

# This part is to use the file input.csv and input2.csv for testing
# list = []
# with open('input.csv', 'r') as csvFile:
#     csvReader = csv.reader(csvFile)
#     next(csvReader)
#     for line in csvReader:
#         list.append(line)
#
# count = 0
# while count < len(list):
#     Needleman(list[count][0], list[count][1])
#     count += 1

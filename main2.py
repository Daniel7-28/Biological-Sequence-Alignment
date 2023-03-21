import sys
import csv
# THIS IS ANOTHER WAY OF IMPLEMENTATION

# This function use Needleman-Wunsch Algorithm to implement global sequence alignment


# Sequence1 is represented by columns & sequence2 is represented by rows
def Needleman(sequence1, sequence2):
    # rowLength is the total amount of columns & columnLength is the total amount of rows
    rowLength = len(sequence1)
    columnLength = len(sequence2)

    # Initializing the matrix and pathMatrix to 0
    matrix = [[0 for rows in range(rowLength+1)] for columns in range(columnLength+1)]
    pathMatrix = [[0 for rows in range(rowLength+1)] for columns in range(columnLength+1)]  # This will store the path

    # initialization step ---- F_0,j = d * j & F_i,0 = d * i,
    d = -2  # this is the gap penalty

    for row in range(columnLength + 1):
        matrix[row][0] = d * row

    for column in range(rowLength+1):
        matrix[0][column] = d * column

    # Calculating max of F_i,j
    for row in range(1, columnLength + 1):
        for column in range(1, rowLength + 1):
            # This make the function of the Scoring Matrix
            if sequence1[column-1] == sequence2[row-1]:
                prevDiagonal = matrix[row - 1][column - 1] + 1
            else:
                prevDiagonal = matrix[row - 1][column - 1] - 1

            prevColumn = matrix[row][column-1] + d
            prevRow = matrix[row-1][column] + d

            matrix[row][column] = max(prevDiagonal, prevColumn, prevRow)

            # selecting the prevColumn 1st, prevRow 2nd and prevDiagonal last if there is a tie
            if max(prevDiagonal, prevColumn, prevRow) == prevColumn:
                pathMatrix[row][column] = 1
            elif max(prevDiagonal, prevColumn, prevRow) == prevRow:
                pathMatrix[row][column] = 2
            else:
                pathMatrix[row][column] = 3

    # Tracing the route

    # sequenceAligned1 represent the second word and sequenceAligned2 represent the first word
    sequenceAligned1 = ""
    sequenceAligned2 = ""

    iTrace = columnLength
    jTrace = rowLength

    # taking action on which path took.
    # 0 if is in the edges of the matrix 1 if is goes horizontal, 2 if is goes vertical and 3 if is goes diagonal
    while iTrace >= 0 and jTrace > 0 or iTrace > 0 and jTrace >= 0:
        if pathMatrix[iTrace][jTrace] == 2:
            sequenceAligned1 = sequence2[iTrace - 1] + sequenceAligned1
            sequenceAligned2 = "-" + sequenceAligned2

            iTrace -= 1
        elif pathMatrix[iTrace][jTrace] == 1:
            sequenceAligned1 = "-" + sequenceAligned1
            sequenceAligned2 = sequence1[jTrace - 1] + sequenceAligned2

            jTrace -= 1
        elif pathMatrix[iTrace][jTrace] == 0 and (iTrace == 0 and jTrace > 0 or jTrace == 0 and iTrace > 0):
            if iTrace == 0:
                sequenceAligned1 = "-" + sequenceAligned1
                sequenceAligned2 = sequence1[jTrace - 1] + sequenceAligned2

                jTrace -= 1
            else:
                sequenceAligned1 = sequence2[iTrace - 1] + sequenceAligned1
                sequenceAligned2 = "-" + sequenceAligned2

                iTrace -= 1
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
# with open('input2.csv', 'r') as csvFile:
#     csvReader = csv.reader(csvFile)
#     next(csvReader)
#     for line in csvReader:
#         list.append(line)
#
# count = 0
# while count < len(list):
#     Needleman(list[count][0], list[count][1])
#     count += 1


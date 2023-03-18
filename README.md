# Biological-Sequence-Alignment
### Project 1 of Analysis of Algorithm and Design Class (ICOM4038/CIIC4025) 

The Goal of project one is to implement your own Needleman-Wunsch algorithm using Dynamic Programming.
As a scoring matrix, the algorithm must use the following:
- Reward on a match: 1 
- Penalty on a mismatch: -1
- Gap penalty: -2

The application must be developed in Python
The application will take as an input file from the command line and will output the sequences alignments for each of the rows on the input file.
The input file will be a comma separated (csv) file with the following format:

**sequence1,sequence2**

**GATTACA,GTCGACGCA**

Your program will align all rows on the file and for each row will produce an output like:

***GATTAC--A GTCGACGCA***

The output will be printed to the standard output, one line for each input row on the file.

You can use this website to understand better what the code do and the and the purpose of this project

https://bioboot.github.io/bimm143_W20/class-material/nw/


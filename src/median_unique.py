from sets import Set
import os, sys, array, bisect

# finds the median of a list of numbers. This is a O(1) operation
def medianOfSortedList(inputList):
    if len(inputList) < 1:
    	return None
    if len(inputList) % 2 == 1:
    	return inputList[((len(inputList) + 1) / 2) - 1] / 1.0
    else:
    	return float(sum(inputList[(len(inputList) / 2) - 1 : (len(inputList) / 2) + 1])) / 2.0

# sets up input and output paths
script_dir = os.path.dirname(__file__)
relativePathOfSrcOfTweets = '../' + sys.argv[1]
relativePathOfDstOfResults = '../' + sys.argv[2]

absPathOfSrcOfTweets = os.path.join(script_dir, relativePathOfSrcOfTweets)
absPathOfDstOfResults = os.path.join(script_dir, relativePathOfDstOfResults)

# this array tracks the unique words. I use an unsigned short representation since it takes up
# 2 bytes of space and we know that the median number of unique words per tweet will be less 
# than 65,535.
listTracker = array.array('H')

distFile = open(absPathOfDstOfResults, 'w')

with open(absPathOfSrcOfTweets, 'r') as inputFile:
    for line in inputFile:
    	# set only accepts unique words
    	listOfUniqueWords = Set(line.split())

        # find and append the length of the unique words into the list tracker while maintaining order
        # insort is a O(log(n)) operation. This boosts out performance as we do not repeatedly sort
        # the array.
        bisect.insort(listTracker, len(listOfUniqueWords))

    	#find the median value of the sorted list tracker
    	medianVal = medianOfSortedList(listTracker)

    	#write value to the output file
    	distFile.write(str(medianVal) + '\n')

distFile.close()



import collections, sys, os

script_dir = os.path.dirname(__file__)
relativePathOfSrcOfTweets = '../' + sys.argv[1]
relativePathOfDstOfResults = '../' + sys.argv[2]

absPathOfSrcOfTweets = os.path.join(script_dir, relativePathOfSrcOfTweets)
absPathOfDstOfResults = os.path.join(script_dir, relativePathOfDstOfResults)

distFile = open(absPathOfDstOfResults, 'w')

tweetTracker = collections.Counter()

# we track the largest word for output formatting reasons. The big-o of this tracking is O(n) and
# the space needed will just be O(1)
largestWordLength = 0

# this method only reads one line at a time, so it does not load the file into memory
with open(absPathOfSrcOfTweets, 'r') as f:
    for line in f:
        for word in line.split():
        	#increment counter based on the word
        	tweetTracker[word] += 1

        	#track the length of the largest word here for formatting purposes
        	lengthOfWord = len(word)
        	if lengthOfWord > largestWordLength:
        		largestWordLength = lengthOfWord

# this is a O(n*log(n)) operation, which is efficient enough for our purpose
for tuple in sorted(tweetTracker.items()):
	word = tuple[0]
	frequency = tuple[1]

	# add 6 spaces after the largest word length to the seperator (based on the output given in the sample result)
	spacesRequired = ' ' * (largestWordLength + 6 - len(word))

	# write value to the output file
   	distFile.write(str(word) + spacesRequired + str(frequency) + '\n')

distFile.close()
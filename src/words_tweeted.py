import collections, sys, os

script_dir = os.path.dirname(__file__)
relativePathOfSrcOfTweets = '../' + sys.argv[1]
relativePathOfDstOfResults = '../' + sys.argv[2]

absPathOfSrcOfTweets = os.path.join(script_dir, relativePathOfSrcOfTweets)
absPathOfDstOfResults = os.path.join(script_dir, relativePathOfDstOfResults)

distFile = open(absPathOfDstOfResults, 'w')

# We use a high performance container structure here to track frequency
tweetTracker = collections.Counter()

# We use the maximum size of a tweet to calculate the space formatting. The size of a
# word will not exceed this.
maximumSizeOfWord = 140

# this method only reads one line at a time, so it does not load the file into memory
with open(absPathOfSrcOfTweets, 'r') as f:
    for line in f:
        for word in line.split():
        	# increment counter based on the word
        	tweetTracker[word] += 1

# this is a O(n*log(n)) operation, which is efficient enough for our purpose
for tuple in sorted(tweetTracker.items()):
	word = tuple[0]
	frequency = tuple[1]

	# add 6 spaces after the largest word length to the seperator (based on the output given in the sample result)
	spacesRequired = ' ' * (maximumSizeOfWord - len(word))

	# write value to the output file
   	distFile.write(str(word) + spacesRequired + str(frequency) + '\n')

distFile.close()
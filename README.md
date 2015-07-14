# Running this project
bash run.sh

The above command will run median_unique.py and words_tweeted.py in the src dir and output results to the f1.txt and f2.txt in tweet_output

# Time taken
3.5 hrs

# Depedencies
1. bisect
2. sets
3. collections

# Assumptions on memory
According to google, there are approximate 500 million tweets generated a day. This comes to about 3.5 billion tweets a week. Both my solutions contain in-memory datastructures, a collection counter in the words_tweeted.py file and a list in the median_unique.py file. 

Assumming 16GB main memory (current settings in my computer), the theoretical maximum space each entry with the in-memory objects can store is ~20 bits (16*2^32/(3.5*10^9)) or 2.5 bytes. For median_unique.py, I used an unsigned short array to store the unique values since each element takes up 2 bytes, less than the 2.5 bytes limit. For words_tweeted.py, I used a high performance container called Counter to iterate. 

I have not formally characterized the memory complexity of container data structure and there doesnt seem to be good documentation online for it, but based on posts in stackoverflow and blogs, the container type seems suitable for high performance in-memory storage.

# Optimizations that were implemented
We did a rolling median calculation of an integer stream to improve performance of median_unique.py. This utilized the bisect library
in python that provides us with an ordered list. It uses a O(log(n)) insert algorithm to maintain a sorted list as streams of integers come through.
Using this technique, our median calculator is O(1) in runtime.


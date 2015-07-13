#!/bin/bash
python src/words_tweeted.py tweet_input/tweets.txt tweet_output/f1.txt
python src/median_unique.py tweet_input/tweets.txt tweet_output/f2.txt
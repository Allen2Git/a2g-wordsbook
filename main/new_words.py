#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020, 04, 14, 05, 40
# @Author  : Allen Zhang
# @File    : ~/a2g-wordsbook/main/new_words.py
# Usage: 

# Default Constant Values:
WORD_CONFIDENCE = 1 # Define the word of threshold AWS Transcribe predicted confidence to choose
NEW_WORDS_FILENAME = "./words/new_words.txt"
BASE_WORDS_FILENAME =  "./words/base_words.txt"
MEDIA_JSON_FILENAME = "./words/media-overview.json"

__version__ = '0.2'
__author__ = "Allen Zhang"

import json
import os
from os.path import dirname, join
from nltk.corpus import wordnet as wn


# Check if the word or its morphy is a new word in base words 
def is_new_word(new_word="", base_words=[]):
    if (str.isalpha(new_word)):
        if wn.synsets(new_word, pos='v') == []:
            morphy_new_word = wn.morphy(new_word)
        else:
            morphy_new_word = wn.morphy(new_word, "v")
        if ((morphy_new_word) != None) and \
            (morphy_new_word not in base_words):
            return morphy_new_word
    else:
        return False


# Write new_words to file for merging
def write_news_words_file(new_words=[],
                            new_words_file_name=NEW_WORDS_FILENAME):    
    new_words_path = join(current_dir, new_words_file_name)
    new_words_str = ""
    with open(new_words_path, "w") as new_words_file:
        for word in new_words:
            new_words_str += word + "\n"
        new_words_file.write(new_words_str)

base_words = [] # base_words for all known words

# read known words from base_words_file
current_dir = dirname(__file__)
base_words_path = join(current_dir,BASE_WORDS_FILENAME)
with open(base_words_path,"r") as base_words_file:
    base_words_lines = base_words_file.read().splitlines()
    word = ""
    for word in base_words_lines:
        base_words.append(word)

new_words = [] # new words from json file from transcribe

# read words from json file generated from transcribe
# TODO: 
# Change json fix name to get from commandline or any other input
# Or abstract this part to a class
new_words_path = join(current_dir, MEDIA_JSON_FILENAME)
with open(new_words_path,"r") as new_words_file:
    new_words_json = json.loads(new_words_file.read())
    for item in new_words_json["results"]["items"]:
        new_word = str.lower(str(item["alternatives"][0]["content"]))
        word_confidence = float(item["alternatives"][0]["confidence"])
        if word_confidence >= WORD_CONFIDENCE:
            # judge if it is a simple punctuation through word length.
            new_word = is_new_word(new_word, base_words)
            if ( new_word and (new_word not in new_words)):
                new_words.append(new_word) # add new word to new_words list
        else:
            continue

# remove known word by search base_words from new_words
# word = ""
# for word in new_words:
#    if word in base_words:
#        new_words.remove(word) 
    
# outpub the new_words:
# TODO - Display new words with more details
# Search new_words in dict then render with word, phonetic, paraphrase，and example

# TODO - Words with confidence
# Tag the words with confidence, decrease the word with low confidence

# TODO - Export a file can be imported by Youdao Dict to better remeber


print("The new words are write into file new_words.txt in folder words\n")
write_news_words_file(new_words)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020, 04, 18, 20, 53
# @Author  : Allen Zhang
# @File    : ~/zhangyang/workspace/a2g-wordsbook/main/a2g-wordsbook.py
# @Description : 
# 


# Default Constant Values:
WORD_CONFIDENCE = 1 # Define the word of threshold AWS Transcribe predicted confidence to choose
NEW_WORDS_FILENAME = "./words/new_words.txt" # new words file or txt file output to
BASE_WORDS_FILENAME =  "./words/base_words.txt" # base words lexicon it's mainly Allen's lexicon
MEDIA_JSON_FILENAME = "./words/media-overview.json" # Default or sample file to process 

__version__ = '0.2'
__author__ = "Allen Zhang"

import json
import os
from os.path import dirname, join
from nltk.corpus import wordnet as wn

# class WordsParse used to parse input file including pure txt, pdf, transcribe json. 
# The instance function will return the de-duplicated words of input file
# class paras as below:
# string(file_name) is input file name
# string(file_type) is one of txt, pdf, transcribe_json.
# return words = [] 
class WordsParse():
	def __init__(self, 
		parse_filename = MEDIA_JSON_FILENAME, 
		file_type = "transcribe_json" 
		):
		self.parse_filename = parse_filename
		self.file_type = file_type
		self.words = []
		self.current_dir = dirname(__file__)
		self.parse_filepath = join(current_dir,self.parse_filename)

		if self.file_type == "txt":
			txt_parse()
		elif self.file_type == "pdf":
			pdf_parse()
		elif self.file_type == "transcribe_json":
			transcribe_json_parse()
		else:
			# TODO throw exception
			pass

	# Check if the word or its morphy is a new word in base words 
	def is_new_word(self,new_word=""):
		if (str.isalpha(new_word)):
			if wn.synsets(new_word, pos='v') == []:
				morphy_new_word = wn.morphy(new_word)
			else:
				morphy_new_word = wn.morphy(new_word, "v")
			if ((morphy_new_word) != None) and \
				(morphy_new_word not in self.words):
				return morphy_new_word
		else:
			return False


	def pdf_parse(self):
	# parse the PDF file like paper to pure txt
		pass

	def transcribe_json_parse(self):
		with open(self.parse_filepath, "r") as parse_file:
			parse_file_json = json.loads(parse_file.read())
			for item in parse_file_json["results"]["items"]:
				new_word = str.lower(str(item["alternatives"][0]["content"]))
				word_confidence = float(item["alternatives"][0]["confidence"])
				if word_confidence >= WORD_CONFIDENCE:
					# judge if it is a simple punctuation through word length.
					new_word = is_new_word(new_word)
					if ( new_word and (new_word not in self.words)):
						self.words.append(new_word) # add new word to new_words list
				else:
					continue


	def txt_parse(self):
		with open(self.parse_filepath, "r") as txt_file:
			self.words = list(set(txt_file.read().splitlines()))


# class Words Output used to output new words to different type like pure_words, \
# trans_words(word with translation), youdao_xml
# Words output direct to a file
class WordsOutput():
	def __init__(self, 
		new_words = [], 
		output_type = "pure_words",
		output_filename = NEW_WORDS_FILENAME
		):
		self.new_words = new_words
		self.output_type = output_type
		self.output_filename = output_filename
		self.current_dir = dirname(__file__)
		self.parse_file_path = join(current_dir,self.output_file_name)
	
		if output_type == "pure_words":
			pure_words_output()
		elif output_type == "trans_words":
			trans_words_output()
		elif output_type == "youdao_xml":
			youdao_xml_output()
		elif output_type == "ddb":
			ddb_output()
		else: # TODO throw exception for unknown param
			pass
			

	def pure_words_output(self):
		new_words_str = ""
		with open(self.parse_file_path, "w") as output_words_file:
			for word in self.new_words:
				new_words_str += word + "\n"
			output_words_file.write(self.parse_file_path)

	def trans_words_output(self):
		pass

	def youdao_xml_output(self):
		pass

	def ddb_output(self):
		pass

# Base Words is Allen's lexicon contained words
# self.base_words is the most often output word list.
class BaseWords():
	def __init__(self,
		base_words_file = BASE_WORDS_FILENAME, 
		base_words_type = "txt"
		):
		self.base_words = []
		self.base_words_filename = base_words_filename
		self.base_words_type = base_words_type

		self.current_dir = dirname(__file__)
		self.base_words_file_path = join(current_dir, self.base_words_filename)

		if base_words_type == "txt":
			get_from_txt()
		elif base_words_type == "ddb":
			get_from_ddb()
		else: # TODO throw new exception
			pass
	
	def get_from_txt(self):
		with open(base_words_file_path,"r") as base_words_file:
			base_words_lines = base_words_file.read().splitlines()
			word = ""
			for word in base_words_lines:
				self.base_words.append(word)

	def get_from_ddb(self):
		pass

	def add_new_words(self):
		pass

	def add_recited_words(self):
		pass

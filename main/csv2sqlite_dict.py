from stardict import StarDict
from os.path import dirname, join
import os

file_path = dirname(__file__)
dict_path = join(file_path,"./dict/star_sqldb.db")
dict = StarDict(dict_path)
word_output = dict.query('given')
out_put = "{} {} \n {} \n".format( word_output['word'], word_output['phonetic'], word_output['translation'])
print(out_put)

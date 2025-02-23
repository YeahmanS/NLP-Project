"""
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

text = "Hi how are you !"
print(word_tokenize(text))

"""
# MORE REGEX 

import re 

print(f"re.match('abc','abcd') : {re.match('abc','abcd')}")
print(f"re.search('abc','abcd') : {re.search('abc','abcd')}")

print("\n using end of string")

print(f"re.match('cd','abcd') : {re.match('cd','abcd')}")
print(f"re.search('cd','abcd') : {re.search('cd','abcd')}")


match_words_and_digits = (r"\d+|\w+")
print(re.findall(match_words_and_digits,'He has 11 cats .'))

my_str =" match lowercase spaces nums like 12, but no commas" 

print(re.match(r"[a-z0-9 ]+",my_str))
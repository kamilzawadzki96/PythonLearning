import random
import string
from random_word import RandomWords
from PyDictionary import PyDictionary

special_signs = '!@#$'

#Tottaly random password
s = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
passlen = 14
p =  "".join(random.sample(s,passlen ))
print(p)

#Password with multiple characters
p = "".join(random.sample(string.ascii_uppercase,1) + random.sample(string.ascii_lowercase,4) + random.sample(special_signs,1) + random.sample(string.digits, 4))
print(p)

#Passowrd with random word
p = RandomWords().get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10).capitalize() + "".join(random.sample(special_signs,1) + random.sample(string.digits, 4))
print(p)

#Meaning of random password
#meaning = PyDictionary.meaning(p)
#print(meaning)
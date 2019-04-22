import pyphonetics as pyp
import weighted_levenshtein as ed
import numpy as np

def data_loading():
    f = open("./data/correct.txt", "r")
    f1 = f.readlines()
    f.close()

    f = open("./data/fake_mis.txt", "r")
    f2 = f.readlines()
    f.close()

    f = open("./data/dict.txt", "r")
    f3 = f.readlines()
    f.close()
    return f1, f2, f3


def write_corrected(temp):
    f = open("./data/soundex_corrected.txt", "w+")
    for element in temp:
        f.write(element)
    f.close()

# A simplified Neighborhood search that only works for 4 digit soundex
# Return a similar word in dict





# Load data
correct, misspell, dic = data_loading()

# Soundex test
soundex = pyp.Soundex()
print(soundex.phonetics('rubert'))
print(soundex.phonetics('ruportkan'))
print('----------------------------')
for element in misspell:
    print(soundex.phonetics(element))
print('----------------------------')
for i in range(0, len(misspell)):
    print(soundex.phonetics(misspell[i]))
print('----------------------------')
print(soundex.distance('rubert', 'ruportd'))


'''
# If misspell does not exist in dict, apply soundex to find most similar word
corrected = []
for element in misspell:
    if element in dic:
        corrected.append(element)
    else:
        misspell_soundex = soundex(element)
        corrected.append(simplified_NS(dict_soundex, misspell_soundex))

# Write corrected to a text file
write_corrected(corrected)
'''



import fuzzy


def data_loading():
    f = open("./data/correct.txt", "r")
    f1 = f.readlines()
    f.close()

    f = open("./data/misspell.txt", "r")
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
def simplified_NS(dict_soundex, misspell_soundex):
    if misspell_soundex in dict_soundex:
        i = dict_soundex.index(misspell_soundex)
    else:
        for code in dict_soundex:
            count = 0
            highest = 0
            highest_code = "None\n"
            for j in range(0, 3):
                if code[j] == misspell_soundex[j]:
                    count = count + 1
            if count > highest:
                highest = count
                highest_code = code
        return highest_code




# Load data
correct, misspell, dic = data_loading()

# Soundex test
soundex = fuzzy.Soundex(4)
dict_soundex = []
for element in dic:
    dict_soundex.append(soundex(element))
print(dict_soundex[1])

soundex = fuzzy.Soundex(4)
misspell_soundex = soundex('a')
print(misspell_soundex)
print(simplified_NS(dict_soundex, misspell_soundex))


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



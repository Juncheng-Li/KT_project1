from collections import Counter


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
    f = open("./data/ngram_corrected.txt", "w+")
    for element in temp:
        f.write(element)
    f.close()


def split(string, length, step=1):
    return (string[0+i:length+i] for i in range(0, len(string), step))


def grams(word, n):
    gram = list(split(word, n))
    if len(gram[-1]) == 1 and len(gram) > 1:
        gram.pop(-1)
    return gram


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def calc(string1, string2):
    gramList1 = grams(string1, 2)
    gramList2 = grams(string2, 2)
    sum = len(gramList1) + len(gramList2)
    set1 = set(gramList1)
    set2 = set(gramList2)
    inter = set1.intersection(set2)
    inter = list(inter)
    intersection = len(inter)

    duplicate1 = Counter(gramList1)
    duplicate2 = Counter(gramList2)
    for element in inter:
        m = duplicate1[element]
        n = duplicate2[element]
        num = min(m, n)
        if num > 1:
            intersection += num - 1

    score = sum - 2 * intersection
    return score


# Load data
correct, misspell, dic = data_loading()

# Start
corrected = []

for i in range(0, len(misspell)):
    if misspell[i] in dic:
        corrected.append(misspell[i])
    else:
        lowest = 1000
        lowest_match = "None\n"
        for d in dic:
            value = calc(misspell[i], d)
            if value == 0:
                lowest_match = d
                break
            if value < lowest:
                lowest = value
                lowest_match = d
        corrected.append(lowest_match)

#print(corrected)
write_corrected(corrected)
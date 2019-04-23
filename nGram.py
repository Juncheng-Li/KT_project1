from collections import Counter


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


def write_corrected(correct, misspell, temp, evaluation):
    f = open("./data/nGram.txt", "w+")
    for a in range(0, len(temp)):
        # f.write(misspell[a].rstrip() + ', ')
        # f.write(correct[a].rstrip() + ' ->[ ')
        temp_list = temp[a]
        for c in temp_list:
            f.write(c.rstrip() + ' ')
        f.write('\n')
    # f.write('Predict p and r, Detection p and r: ')
    # f.write(str(evaluation[0]) + ' ')
    # f.write(str(evaluation[1]))
    f.close()


def write_corrected_verbose(correct, misspell, temp, evaluation):
    f = open("./data/nGram_verbose.txt", "w+")
    for a in range(0, len(temp)):
        f.write(misspell[a].rstrip() + ', ')
        f.write(correct[a].rstrip() + ' ->[ ')
        temp_list = temp[a]
        for c in temp_list:
            f.write(c.rstrip() + ' ')
        f.write(']\n')
    f.write('Predict p and r, Detection p and r: ')
    f.write(str(evaluation[0]) + ' ')
    f.write(str(evaluation[1]))
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
    interse = len(inter)

    duplicate1 = Counter(gramList1)
    duplicate2 = Counter(gramList2)
    for element in inter:
        m = duplicate1[element]
        n = duplicate2[element]
        num = min(m, n)
        if num > 1:
            interse += num - 1

    score = sum - 2 * interse
    return score


def predict_evaluation(correct, best_matches):
    tp = 0
    tp_n_fp = 0
    for i in range(0, len(best_matches)):
        if correct[i] in best_matches[i]:
            tp += 1
        tp_n_fp += len(best_matches[i])
    precision = tp / tp_n_fp
    tp_n_fn = len(best_matches)
    recall = tp / tp_n_fn
    return precision, recall, tp, tp_n_fp, tp_n_fn


def detect_evaluation(correct, misspell, best_matches):
    tp = 0
    fn = 0
    tn = 0
    fp = 0
    for e in range(0, len(best_matches)):
        if correct[e] == misspell[e] and misspell[e] in best_matches[e]:
            tp += 1
        if correct[e] != misspell[e] and misspell[e] not in best_matches[e]:
            fn += 1
        if correct[e] == misspell[e] and misspell[e] not in best_matches[e]:
            tn += 1
        if correct[e] != misspell[e] and misspell[e] in best_matches[e]:
            fp += 1

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    return precision, recall


# Load data
correct, misspell, dic = data_loading()

# Start
best_matches = []
for i in range(0, len(misspell)):
    score = []
    lis = []
    if misspell[i] in dic:
        best_matches.append([misspell[i]])
    else:
        for d in dic:
            value = calc(misspell[i], d)
            score.append(value)
        best = min(score)
        indices = [i for i, val in enumerate(score) if val == best]
        for j in indices:
            lis.append(dic[j])
        best_matches.append(lis)

print(best_matches)
pred_evaluation = predict_evaluation(correct, best_matches)
det_evaluation = detect_evaluation(correct, misspell, best_matches)
eva = []
eva.append(pred_evaluation)
eva.append(det_evaluation)
write_corrected(correct, misspell, best_matches, eva)
write_corrected_verbose(correct, misspell, best_matches, eva)

import weighted_levenshtein as ed
import numpy as np
import time


def edit_distance(word1, word2):
    return ed.levenshtein(word1, word2)


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
    f = open("./data/ED.txt", "w+")
    for a in range(0, len(temp)):
        temp_list = temp[a]
        for c in temp_list:
            f.write(c.rstrip() + ' ')
        f.write('\n')
    f.close()


def write_corrected_verbose(correct, misspell, temp, evaluation):
    f = open("./data/ED_verbose.txt", "w+")
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
    return precision, recall


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
    for d in dic:
        # Calculates Edit Distance between misspell token
        # and every word in dictionary to get a list of
        # distance values
        value = edit_distance(misspell[i], d)
        score.append(value)
    # Get the lowest distance among the list
    best = min(score)
    # Get indices of all the words having lowest distance
    indices = [i for i, val in enumerate(score) if val == best]
    # Get all the word having the lowest distance
    # by their index and append them in a list
    for j in indices:
        lis.append(dic[j])
    best_matches.append(lis)


# Calculates the prediction value
pred_evaluation = predict_evaluation(correct, best_matches)
print("Precision: " + str(pred_evaluation[0]))
print("Recall: " + str(pred_evaluation[1]))

# Write results to files
write_corrected(correct, misspell, best_matches, pred_evaluation)
write_corrected_verbose(correct, misspell, best_matches, pred_evaluation)

# Prints total processing time of the program
print(time.clock())

# All correctly changed / All changed by the program
def correction_precision(correct_path, corrected_path, misspell_path):
    f1 = open(correct_path, 'r')
    correct_list = f1.readlines()
    f1.close()

    f2 = open(corrected_path, 'r')
    corrected_list = f2.readlines()
    f2.close()

    f3 = open(misspell_path, 'r')
    misspell_list = f3.readlines()
    f3.close()

    # print(correct_list[4])
    # print(corrected_list[4])
    changed = 0
    changed_index = []
    correctly_changed = 0
    for i in range(0, len(corrected_list)):
        if corrected_list[i] != misspell_list[i]:
            changed += 1
            changed_index.append(i)
    # print(changed)
    # print(changed_index)

    for j in changed_index:
        print(corrected_list[j] + correct_list[j])
        if corrected_list[j] == correct_list[j]:
            correctly_changed += 1
    # print(correctly_changed)

    precision = correctly_changed / changed
    return precision


# In reported change, how many really need change: really need change / all change
def detection_precision(correct_path, corrected_path, misspell_path):
    f1 = open(correct_path, 'r')
    correct_list = f1.readlines()
    f1.close()

    f2 = open(corrected_path, 'r')
    corrected_list = f2.readlines()
    f2.close()

    f3 = open(misspell_path, 'r')
    misspell_list = f3.readlines()
    f3.close()

    changed = 0
    changed_index = []
    need_change = 0
    for i in range(0, len(misspell_list)):
        if corrected_list[i] != misspell_list[i]:
            changed += 1
            changed_index.append(i)

    for j in changed_index:
        if correct_list[j] != misspell_list[j]:
            need_change += 1

    return need_change / changed


# changed / All need change
def detection_recall(correct_path, corrected_path, misspell_path):
    f1 = open(correct_path, 'r')
    correct_list = f1.readlines()
    f1.close()

    f2 = open(corrected_path, 'r')
    corrected_list = f2.readlines()
    f2.close()

    f3 = open(misspell_path, 'r')
    misspell_list = f3.readlines()
    f3.close()

    changed = 0
    all_need_change = 0
    for i in range(0, len(misspell_list)):
        if corrected_list[i] != misspell_list[i]:
            changed += 1

    for j in range(0, len(misspell_list)):
        if correct_list[j] != misspell_list[j]:
            all_need_change += 1

    return changed / all_need_change


# Give path of data sets
correct_path = './data/correct.txt'
corrected_path = './data/ngram_corrected.txt'
misspell_path = './data/misspell.txt'

# Calculate precisions and recall
print(correction_precision(correct_path, corrected_path, misspell_path))
print(detection_precision(correct_path, corrected_path, misspell_path))
print(detection_recall(correct_path, corrected_path, misspell_path))


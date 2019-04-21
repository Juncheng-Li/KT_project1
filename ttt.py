else:
if len(misspell_soundex) == 1:
    for code1 in dict_soundex:
        if misspell_soundex[0] == code1[0]:
            return dict_soundex.index(code1)
        else:
            continue

if len(misspell_soundex) == 2:
    highest = 0
    highest_word = "None\n"
    for code2 in dict_soundex:
        count = 0
        for i in range(0, min(len(code2), len(misspell_soundex))):
            if misspell_soundex[i] == code2[i]:
                count = count + 1
        if count == 2:
            highest_word = code2
            break
        if count > highest:
            highest = count
            highest_word = code2
    return dict_soundex.index(highest_word)

if len(misspell_soundex) == 3:
    highest = 0
    highest_word = "None\n"
    for code3 in dict_soundex:
        count = 0
        count2 = 0
        for i in range(0, min(len(code3), len(misspell_soundex))):
            if misspell_soundex[i] == code3[i]:
                count = count + 1
        if len(misspell_soundex) == 4:
            for j in range(0, 3):
                if misspell_soundex[j] == code3[j + 1]:
                    count2 = count2 + 1
        count = max(count, count2)
        if count == 3:
            highest_word = code3
            break
        if count > highest:
            highest = count
            highest_word = code3
    return dict_soundex.index(highest_word)

if len(misspell_soundex) == 4:
    highest = 0
    highest_word = "None\n"
    for code4 in dict_soundex:
        count = 0
        count2 = 0
        for i in range(0, min(len(code4), len(misspell_soundex))):
            if misspell_soundex[i] == code4[i]:
                count = count + 1
        if len(misspell_soundex) == 3:
            for j in range(0, 3):
                if misspell_soundex[j] == code4[j + 1]:
                    count2 = count2 + 1
        count = max(count, count2)
        if count == 4:
            highest_word = code4
            break
        if count > highest:
            highest = count
            highest_word = code4
    return dict_soundex.index(highest_word)
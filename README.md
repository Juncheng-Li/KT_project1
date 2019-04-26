# KT_project1

The project applied three algorithms on the spelling corrction task, including Edit Distance(Levenshtain Distance), Bigram, and Soundex.

Each algorithm is written in a stand-alone python file.

ED.py:
Predicts the correct word by calculating the Edit distance between token and words in the dictionary.

edit_distance(word1, word2): Calculates the edit_distance between two words


nGram.py:
Predicts the correct word by splitting the token into substrings of two letters.

Splits(string, length, step=1) and grams(word, n): splits words into substrings of n letters, in this project n = 2.
intersection(lst1, lst2): Counts how many grams in common
calc(String1, String): Calculates the Bigram score


Soundex.py:
Converts word into Soundex code first, then apply Edit Distance to calculate the similarity between words.

soundex_distance(word1, word2): Converts words into Soundex code and then calculates the Soundex distance.


Each file has following functions:

data_loading:
Loads data from misspell.txt, correct.txt, dict.txt and store them respectively in three lists.

write_corrected:
Store word predictions in a file

write_corrected_verbose:
Store word predictions as well as corresponding correct and misspell words in a file

predict_evaluation:
Calculates precision and recall of the prediction








External libraries used in this project:

weighted-levenshtein for calculating edit distance and neighbourhood search:
https://weighted-levenshtein.readthedocs.io/en/master/

jellyfish for calculating soundex:
https://pypi.org/project/jellyfish/

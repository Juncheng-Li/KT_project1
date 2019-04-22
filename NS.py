import weighted_levenshtein as ed
import numpy as np

insert_costs = np.ones(128, dtype=np.float64)
delete_costs = np.ones(128, dtype=np.float64)
substitute_costs = np.ones((128, 128), dtype=np.float64)


def neighborhood_search(word1, word2):
    return ed.levenshtein(word1, word2, insert_costs=insert_costs, delete_costs=delete_costs,
                          substitute_costs=substitute_costs)


print(neighborhood_search('lended', 'commodity'))
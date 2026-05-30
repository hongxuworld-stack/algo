# 734. Sentence Similarity

# You are given two sentences, sentence1 and sentence2, represented as arrays of words.

# You are also given a list of similar word pairs, similarPairs, where each pair [word1, word2] means word1 and word2 are similar.

# Two sentences are similar if:

# 1. They have the same length.
# 2. For every index i, sentence1[i] and sentence2[i] are either:
#    - exactly the same word, or
#    - directly listed as a similar pair in similarPairs.

# The similarity relation is symmetric.
# This means if "great" is similar to "fine", then "fine" is also similar to "great".

# However, the similarity relation is not transitive.
# This means if "great" is similar to "good" and "good" is similar to "fine",
# "great" is not necessarily similar to "fine".

# Return true if the two sentences are similar, otherwise return false.
from typing import List
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
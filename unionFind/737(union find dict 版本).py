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
        parent = {}
        size = {}
        def add(x):
            if x not in parent:
                parent[x] = x
                size[x] = 1
        def find(x):
            add(x)
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]
            return True
        l1 = len(sentence1)
        l2 = len(sentence2)
        if l1 != l2:
            return False
        for p1,p2 in similarPairs:
            union(p1,p2)
        for i in range(l1):
            p1 = find(sentence1[i])
            p2 = find(sentence2[i])
            if p1 != p2:
                return False
        return True

# Time: O((p + s) * alpha(w)), where p = len(similarPairs),
# s = len(sentence1), and w is the number of unique words seen.
# Space: O(w)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        counter_1 = [0] * 26
        counter_2 = [0] * 26

        for i in range(n1):
            counter_1[ord(s1[i]) - ord('a')] += 1
            counter_2[ord(s2[i]) - ord('a')] += 1

        if counter_1 == counter_2:
            return True

        for right in range(n1, n2):
            left = right - n1

            counter_2[ord(s2[right]) - ord('a')] += 1
            counter_2[ord(s2[left]) - ord('a')] -= 1

            if counter_1 == counter_2:
                return True

        return False
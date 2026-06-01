class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]
        count = n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            nonlocal count
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                if size[root_a] < size[root_b]:
                    root_a , root_b = root_b, root_a
                parent[root_b] = root_a
                size[root_a] += size[root_b]
                count -= 1
        def is_similar(stra,strb):
            diff_count = 0
            for i in range(len(stra)):
                cha = stra[i]
                chb = strb[i]
                if cha != chb:
                    diff_count += 1
                if diff_count > 2:
                    return False
            return True
        for i in range(n):
            for j in range(i+1,n):
                if is_similar(strs[i],strs[j]):
                    union(i,j)
        return count

# Time: O(n^2 * k), where n = len(strs), k = len(strs[0])
# Space: O(n)
    
# 时间复杂度：
# O(n^2 * k)
# 其中 n = len(strs)，k = len(strs[0])。
# 空间复杂度：
# O(n)
# 因为 parent 和 size 都是长度 n。

# 305. Number of Islands II
# You are given an empty 2D grid of size m x n.
# Initially, all cells are water.
# You are also given an array positions, where positions[i] = [row, col].
# Each position represents adding land to the grid at that cell.
# After each land addition, return the number of islands in the grid.
# An island is formed by connecting adjacent lands horizontally or vertically.
# Diagonal connections do not count.
# Return an array answer, where answer[i] is the number of islands after the i-th land addition.
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
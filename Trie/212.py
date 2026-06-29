class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self,board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        root = TrieNode()
        res = []
        for word in words:
            cur =  root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.word = word
        
        def dfs(r,c,node):
            ch = board[r][c]
            if ch not in node.children:
                return
            node = node.children[ch]
            if node.word:
                res.append(node.word)
                node.word = None
            board[r][c] = "#"
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] != "#":
                    dfs(nr,nc,node)
            board[r][c] = ch
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)
        return res
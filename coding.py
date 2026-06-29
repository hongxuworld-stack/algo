class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_world = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in  cur.children:
                 cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_world = True

    def search(self, word: str) -> bool:
        def dfs(node,index):
            if index == len(word):
                return node.is_world
            ch = word[index]
            if ch != ".":
                if ch in node.children:
                    return dfs(node.children[ch],index+1)
                else:
                    return False
            elif ch  == ".":
                for key in node.children:
                    if dfs(node.children[key],index+1):
                        return True
                return False
        return dfs(self.root,0)
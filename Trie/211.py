class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True


    def search(self, word: str) -> bool:
        def dfs(node,index):
            if index == len(word):
                return node.is_word
            ch = word[index]
            if ch != ".":
                if ch not in node.children:
                    return False
                node = node.children[ch]
                return dfs(node,index+1)
            elif ch ==".":
                for _,child in node.children.items():
                    if dfs(child,index+1):
                        return True
                return False
        return dfs(self.root,0) 
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
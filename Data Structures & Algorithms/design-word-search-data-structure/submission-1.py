class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:

        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWordEnd = True

    def search(self, word: str) -> bool:

        def dfs(cur, i):

            if i == len(word):
                return cur.isWordEnd

            c = word[i]
            if c == '.':
                for child_node in cur.children.values():
                    if dfs(child_node, i + 1):
                        return True

            if c not in cur.children:
                return False
            return dfs(cur.children[c], i + 1)

        cur = self.root
        return dfs(cur, 0)



            





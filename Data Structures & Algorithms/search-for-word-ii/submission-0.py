class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self._build_trie(words)

    def _build_trie(self, words):

        for word in words:
            self._insert(word)

    def _insert(self, word):
        
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWordEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        ROWS, COLS = len(board), len(board[0])
        trie = Trie(words)
        
        ret = set()
        path = []
        def dfs(r, c, cur):

            if cur.isWordEnd:
                ret.add(''.join(path.copy()))

            if ((r < 0 or r >= ROWS) or
                (c < 0 or c >= COLS) or
                board[r][c] == "#" or    
                board[r][c] not in cur.children
            ):
                return

            char = board[r][c]
            path.append(char)
            board[r][c] = "#"

            child = cur.children[char]
            dfs(r + 1, c, child)
            dfs(r, c + 1, child)
            dfs(r - 1, c, child)
            dfs(r, c - 1, child)
            
            board[r][c] = char
            path.pop()
            return

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root)

        return list(ret)




        

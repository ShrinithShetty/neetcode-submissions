class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}


        for word in words:
            d = trie
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]

            d['.'] = word

        rows, col = len(board), len(board[0])
        visit = set()
        res = []

        def dfs(r,c,node):
            if (r < 0 or c < 0 or r >= rows or c >= col or (r,c) in visit or board[r][c] not in node):
                return 

            visit.add((r,c))
            node = node[board[r][c]]

            if '.' in node:
                res.append(node['.'])
                del node['.']

            dfs(r+1,c,node)
            dfs(r-1,c,node)
            dfs(r,c+1,node)
            dfs(r,c-1,node)

            visit.remove((r,c))


        for r in range(rows):
            for c in range(col):
                dfs(r,c,trie)

        return res


        
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1),len(w2))

            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break


        res = []
        visit = {}


        def dfs(i):
            if i in visit:
                return visit[i]
            
            visit[i] = True

            for nei in adj[i]:
                if dfs(nei):
                    return True
            
            visit[i] = False

            res.append(i)





        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "" .join(res)
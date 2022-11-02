class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        bank = set(wordList)
        que = deque([(1, beginWord)])
        visited = set()
        if endWord not in bank:
            return 0
        while que:
            step, word = que.popleft()
            temp = list(word)
            
            for i in range(len(word)):
                for char in [chr(i) for i in range(97, 123)]:
                    new_word = "".join(temp[:i]+[char]+temp[i+1:])
                    if new_word in bank and new_word not in visited:
                        if new_word == endWord:
                            return step+1
                        que.append((step+1, new_word))
                        visited.add(new_word)
        return 0
                        
                    
                
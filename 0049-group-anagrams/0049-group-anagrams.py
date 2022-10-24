class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()
        
        for pos, word in enumerate(strs):
            cpyWord = "".join(sorted(word))
            if cpyWord in seen:
                seen[cpyWord].append(word)
            else:
                seen[cpyWord] = [word]
                
        return [values for _, values in seen.items()]                
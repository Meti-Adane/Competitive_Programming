# question url : https://leetcode.com/problems/making-file-names-unique/

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        hmap = dict()
        for pos, word  in enumerate(names):
            if hmap.get(word) ==None:
                hmap[word] = 0
            else:
                count = hmap[word]
                temp = word
                while hmap.get(temp) != None:
                    count += 1
                    temp = word + "(" + str(count) + ")"
                hmap[temp] = 0
                hmap[word] = count
                names[pos] = word + "(" + str(count) + ")"
        return names
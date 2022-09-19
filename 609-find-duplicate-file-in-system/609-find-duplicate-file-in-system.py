class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = []
        hashmap = dict() # content : [ Paths]
        ans = []
        for i, path in enumerate(paths):
            arr = path.split()
            dirname = arr[0]
            for file in arr[1:]:
                filename, content = file.split("(")
                content.rstrip()
                if content not in hashmap:
                    hashmap[content] = []
                hashmap[content].append(dirname+"/"+filename)
                
        for _, files in hashmap.items():
            if len(files) >= 2:
                ans.append(files)
        return ans
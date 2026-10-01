class WordDictionary:
    def __init__(self):

        self.root = {
            "children": {},
            "is_word": False
        }
        

    def addWord(self, word: str) -> None:
        
        curr = self.root
        for c in word:
            if not c in curr["children"]:
                curr["children"][c] = {
                    "children": {},
                    "is_word": False
                }
            curr = curr["children"][c]
        curr["is_word"] = True
            

    def search(self, word: str) -> bool:

        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c  = word[i]

                if c == ".":
                    for child in curr["children"].values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr["children"]:
                        return False
                    curr = curr["children"][c]
            return curr["is_word"] 

        # def dfs(curr, i):            
        #     if word[i] == ".":
        #         temp = curr["children"]
        #         for key, value in curr["children"].items():
        #             curr = temp[key]
        #             is_word = dfs(curr, i+1)
        #             if is_word:
        #                 return True
        #         return False

        #     if not word[i] in curr["children"]:
        #         return False
            
        #     curr = curr["children"][word[i]]
        #     return dfs(curr, i+1)
        return dfs(0, self.root)
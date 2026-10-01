class PrefixTree:

    def __init__(self):

        self.root = {
            "children" : {},
            "is_word": False
        }

    def insert(self, word: str) -> None:

        curr = self.root
        for c in word:
            if  c not in curr["children"]:
                curr["children"][c] = {
                    "children" : {},
                    "is_word": False
                }

            curr = curr["children"][c]
        curr["is_word"] = True

    def search(self, word: str) -> bool:

        curr = self.root

        for c in word:
            if not c in curr["children"]:
                return False
            
            curr = curr["children"][c]
        return curr["is_word"]
        

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for c in prefix:
            if not c in curr["children"]:
                return False
            
            curr = curr["children"][c]
        return True
        
        
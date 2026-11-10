class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        cell = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }


        res = []
        def backtrack(idx, char):
            if len(char) == len(digits) and char != "":
                res.append(char)
                return
            
            if idx >= len(digits):
                return
            

            for c in cell[digits[idx]]:
                backtrack(idx + 1, char + c)
        

        backtrack(0, "")

        return res
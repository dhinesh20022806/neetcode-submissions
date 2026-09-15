class Solution:
    def isValid(self, s: str) -> bool:
        
        hashMap = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }

        stack = []

        for i in range(len(s)):

            if len(stack) > 0:
                print(stack[len(stack) - 1], hashMap.get(s[i]))

            if len(stack) > 0 and stack[len(stack) - 1] == hashMap.get(s[i]) :
                stack.pop()
            else:
                stack.append(s[i])
        

        return len(stack) == 0
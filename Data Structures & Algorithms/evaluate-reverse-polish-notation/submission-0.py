class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        


        stack = []

        for token in tokens:

            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:

                if token == "+":
                    secondNumber = stack.pop()
                    firstNumber = stack.pop()
                    stack.append(firstNumber + secondNumber)
                
                if token == "-":
                    secondNumber = stack.pop()
                    firstNumber = stack.pop()
                    stack.append(firstNumber - secondNumber)

                if token == "*":
                    stack.append(stack.pop() * stack.pop())
                if token == "/":
                    stack.append(stack.pop() // stack.pop())
        return stack[-1]
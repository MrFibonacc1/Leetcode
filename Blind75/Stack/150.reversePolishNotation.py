class Solution:
    def evalRPN(self, tokens: list[str]) ->int:
        numbers = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                numbers.append(int(i))
            else:
                numberTwo = numbers.pop()
                numberOne = numbers.pop()
                if i == "+":
                    numbers.append(numberOne + numberTwo)
                elif i == "-":
                    numbers.append(numberOne - numberTwo)
                elif i == "*":
                    numbers.append(numberOne * numberTwo)
                else:
                    numbers.append(int(numberOne / numberTwo))
        return numbers[0]

Solution = Solution()
print(Solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
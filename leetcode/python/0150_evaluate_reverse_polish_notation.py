class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operations = {
            "+": lambda a, b: a + b,
            "*": lambda a, b: a * b,
            "-": lambda a, b: b - a,
            "/": lambda a, b: b / a
        }

        for i in range(len(tokens)):
            if tokens[i] not in "+*-/": stk.append(int(tokens[i]))
            else:
                num1 = int(stk.pop())
                num2 = int(stk.pop())
                op = operations[tokens[i]]
                stk.append(op(num1, num2))
        return int(stk[-1])
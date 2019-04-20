class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return
        ops = {"+", "-", "*", "/"}
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                tokens[i] = int(tokens[i])
        stack = []
        for x in tokens:
            if x not in ops:
                stack.append(x)
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                if x == "+":
                    y = top2 + top1
                elif x == "-":
                    y = top2 - top1
                elif x == "*":
                    y = top2 * top1
                elif x == "/":
                    y = top2 / top1
                    y = y + 1 if y < 0 else y
                stack.append(y)
        return stack[-1]


if __name__ == "__main__":
    input = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    solution = Solution()
    print solution.evalRPN(input)
    x = [1, 22]
    x.pop()

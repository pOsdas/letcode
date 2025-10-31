class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = num = 0
        sign = 1  # 1 for '+' -1 for '-'
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)

            elif i == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                num = 0
                sign = 1

            elif i == ')':
                result += sign * int(num)
                result *= stack.pop()
                result += stack.pop()
                num = 0

            elif i == '-':
                result += sign * int(num)
                sign = -1
                num = 0

            elif i == '+':
                result += sign * int(num)
                sign = 1
                num = 0

        result += sign * num
        return result

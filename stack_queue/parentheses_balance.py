
def isCorrectParentheses(s):
    stack = []
    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        elif (not stack) or (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '['):
            return 'No'
        else:
            stack.pop()
    return 'Yes' if len(stack) == 0 else 'No'


if __name__ == "__main__":
    n = int(input())
    out = []
    for _ in range(n):
        s = input()
        out.append(isCorrectParentheses(s))
    for val in out:
        print(val)


# def find(string, k):
#     stack = []
#     for char in string:
#         if stack and (stack[-1][-1] == char):
#                 stack[-1] += char
#                 if len(stack[-1]) == k:
#                     stack.pop()
#         else:
#             stack.append(char)
#
#     return ''.join(stack)
#
#
# print(find("abboa", 2))






def func(s):
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
        out.append(func(s))
    for val in out:
        print(val)

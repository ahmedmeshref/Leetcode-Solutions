def simplifyPath(path: str) -> str:
    f_path = path.split("/")

    # reading and spliting the string
    stack = []
    for w in f_path:
        # skip . and ''
        if w == '' or w == '.':
            continue
        elif w == '..':
            if stack:
                stack.pop()
            continue
        stack.append(w)

    simple_path = "/".join(stack)
    return '/' + simple_path


print(simplifyPath("/home/c"))
print(simplifyPath("/../"))
print(simplifyPath("///home//foo/"))

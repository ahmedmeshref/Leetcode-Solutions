def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l != r:
        if not s[l].isalpha():
            l += 1
        elif not s[r].isalpha():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return s[l] == s[r]


print(isPalindrome("A man, a plan, a canal: Panama"))

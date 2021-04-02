def isPalindrome(s):
    def toChars(s):
        result = ''
        s = s.lower()
        for char in s:
            if char in "abcdefghijklmnopqrstuvwxyz":
                result += char
        return result
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))


print(isPalindrome("Do Good"))
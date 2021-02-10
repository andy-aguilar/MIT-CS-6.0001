def isIn(str1, str2):
    if str1 in str2 or str2 in str1:
        return True
    else:
        return False

print(str(isIn("hello", "chicago")))
print(str(isIn("hi", "chicago")))
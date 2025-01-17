def strStr(haystack: str, needle: str):
    lenhay = len(haystack)
    lenneed = len(needle)
    if needle not in haystack:
        return -1
    else:
        for i in range(0,lenhay,lenneed):
            if haystack[i:i+lenneed] == needle:
                return i
print(strStr("sadbutsad","but"))

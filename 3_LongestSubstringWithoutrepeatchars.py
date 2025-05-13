def lengthOfLongestSubstring(s: str) -> int:
    l = r = 0
    maxsize = 0
    while r != len(s):
        maxsize = max(r-l,maxsize)
        if len(set(s[l:r])) == len(s[l:r]):
            r+=1
        else:
            l+=1
    return maxsize

print(lengthOfLongestSubstring("au"))

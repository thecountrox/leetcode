def checkInclusion( s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
            return False
    else:
            _hash = {chr(num): 0 for num in range(97, 123)}
            _hash2 = {chr(num): 0 for num in range(97, 123)}
            for i in range(len(s1)):
                _hash[s1[i]] +=1
            
            l = 0
            r = len(s1)
            for i in range(l,r):
                    _hash2[s2[i]] +=1
            if _hash == _hash2:
                return True

            def check(a:chr, b:chr, _hash, _hash2)-> bool:
                _hash2[a]-=1
                _hash2[b]+=1
                return _hash == _hash2
                
            while r!=len(s2)+1:
                if check(s2[l],s2[r-1],_hash,_hash2):
                    return True
                else:
                    l+=1
                    r+=1
            return False
print(checkInclusion("ab","eidbaooo"))

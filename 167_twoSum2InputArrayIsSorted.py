def twoSum(numbers: list ,target: int)-> list:
    l = 0 
    r = len(numbers)-1
    while l<r:
        if l+r==target:
            break
        elif l+r > target:
            r-=1
        else:
            l+=0
    return [l,r]

print(twoSum([2,7,11,15],9))

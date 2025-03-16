def productExceptSelf(nums: list) -> list:
    res = []
    def multiexp(i: int, num: list):
        mul = 1
        for j in range(len(num)):
            if i!=j:
                mul*=num[j]
        return mul

    for i in range(len(nums)):
        res.append(multiexp(i,nums))
    return res

print(productExceptSelf([1,2,3,4]))

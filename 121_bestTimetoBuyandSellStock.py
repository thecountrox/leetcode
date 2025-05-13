def maxProfit( prices: list)-> int:
    # brute force
    maxprofit = -float('inf')
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            maxprofit = max(maxprofit, prices[j]-prices[i])

    return maxprofit

print(maxProfit([7,6,4,3,1]))

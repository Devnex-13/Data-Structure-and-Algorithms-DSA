def maxProfit(prices):
  l = 0
  n = len(prices)
  r=l+1
  max_profit = 0

  while r<n:
      if prices[l]>prices[r]:
          min_price = prices[r]
          l = r
      else:
          max_profit = max(max_profit, prices[r]-prices[l])
      r+=1
  return max_profit

a = [1,2,3,4,5,2,6]
print(maxProfit(a))
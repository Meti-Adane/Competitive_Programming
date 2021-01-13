def maximumToys(prices, k):
    count = 0
    price_total = 0
    occurrence = [0] * (k+1)
    sorted_price=[]
    for i in range (len(prices)):
        if prices[i] <= k:
            occurrence[prices[i]] += 1
    for i in range (len(occurrence)):
        if occurrence[i] > 0:
            sorted_price.append(i)
    for i in prices:
        price_total += i
        if price_total >= k:
            return count
        count += 1
    return count

# nk = input().split()
#
# n = int(nk[0])
#
# k = int(nk[1])
#
prices = list(map(int, input().rstrip().split()))

r =100000

result = maximumToys(prices, r)
print(result)
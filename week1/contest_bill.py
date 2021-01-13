# def bonAppetit(bill, k, b):
#     if 2<= len(bill) <= 10 **5 and 0 <= b<= sum(bill):
#         if 0 < k < len(bill):
#             anna_bill = 0
#             m = 0
#             for i in bill:
#                 if 0<= bill[m] <= 10**4:
#                     if i != bill[k]:
#                         anna_bill += i
#                 m +=1
#             anna_share = anna_bill / 2
#             if anna_share == b:
#                 print("Bon Appetit")
#             elif b > anna_share:
#                 print(int(b - anna_share))
#
# nk = input().rstrip().split()
#
# n = int(nk[0])
#
# k = int(nk[1])
#
# bill = list(map(int, input().rstrip().split()))
#
# b = int(input().strip())
#
# bonAppetit(bill, k, b)
# print( % 48)








def divisibleSumPairs(n, k, ar):
    n = len(ar)
    no_of_pairs = 0

    for i in range(n - 1):
        for j in range(n):
            print(i, j)
            if i < j:

                n = ar[i]
                m  = ar[j]
                sum = n + m
                if (sum % k ) == 0:
                    no_of_pairs += 1
    print(no_of_pairs)
nk = input().split()

n = int(nk[0])

k = int(nk[1])

ar = list(map(int, input().rstrip().split()))
divisibleSumPairs(n, k, ar)


# def repeatedString(s, n):
#     word = s
#     i = 0
#     while len(word) < n:
#         word += s[i]
#         i+=1
#         if i > len(s) -1:
#             i = 0
#     no_of_a = word.count("a")
#     return no_of_a
#
# s = input()
# n = int(input())
# print(repeatedString(s, n))

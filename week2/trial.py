#
# import math
#
#
# def checkPossibility(nums) -> bool:
#     i = 0
#     n = 0
#     edit = []
#     while i < (len(nums)):
#             for k in range(i+1, len(nums)-1):
#
#                 print(nums[i], nums[k], nums[k + 1], "====> i =", nums[i])
#                 if (nums[i] > nums[k] and nums[i] > nums[k+1]):
#                     print(nums[i], nums[k], nums[k+1], "====> i =", nums[i])
#                     edit.append(nums[i])
#                 elif (nums[i] > nums[k] and nums[i] < nums[k+1]):
#                     print(nums[i], nums[k], nums[k + 1], "=====> k =", nums[k])
#                     edit.append(nums[k])
#                 # elif (nums[i] < nums[k] and nums[i] > nums[k+1]):
#                 #     edit.append(nums[i])
#
#             i+=1
#     print(edit)
#     return len(edit) <= 1
# #
# # #
# # l = [1, 2, 3, 4, 5]
# # g = [1,2, 3, 4, 7, 2, 3]
# # h = [3, 4, 2, 6]
# # # print(checkPossibility(h))
# # # if i > 0 and abs(nums[i-1] - nums[i+1]) == 1:
# # #     return False
# #
# # r = [
# #     [0, 1], [3, 2], [2, 0]
# # ]
# # print(r[-1][0])
# #
# # def countDown(n):
# #     if n == 1:
# #         return n
# #     else:
# #         r = countDown(n-1)
# #         print(r)
# # countDown(5)
#
# e = 2
# l = [1, 2,3 ,4, 5, 6, 7, 8, 9]
# print(l[e-3:e])

fr = [1, 2, 2, 8, 4, 5]
print(fr[len(fr)//2], fr[len(fr)//2 -1])
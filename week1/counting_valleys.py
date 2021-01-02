#
# def counter(steps,path):
#     valid=True
#     for i in path:
#         if i not in 'UD':
#             valid=False
#             break
#     if steps<2 or steps>10**6 or len(path)!=steps or valid==False:
#         print("invalid input")
#         return()
#     slope=0
#     valley=0
#     for i in path:
#         if i=='U':
#             slope +=1
#         elif i=='D':
#             slope -=1
#         if i=='U' and slope==0:
#             valley +=1
#     return(valley)
# print(counter(8,input()))



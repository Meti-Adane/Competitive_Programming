def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def fib_iterative(n):
    nums = []
    nums.insert(0, 1)
    nums.insert(0, 1)
    if n == 1:
        return 1
    elif n == 0:
        return 0
    for i in range(2, n):
        nums.append(nums[i - 1] + nums[i - 2])
    return nums[-1]
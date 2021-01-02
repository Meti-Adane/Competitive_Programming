
def target_sum(nums, target):
    for i in range(len(nums)-1):
        j = i + 1
        while j <= (len(nums)-1):
            sum = nums[i] + nums[j]
            if sum == target:
                return i, j
            j += 1
nums = [3,2,4]
target = 6
print(target_sum(nums, target))
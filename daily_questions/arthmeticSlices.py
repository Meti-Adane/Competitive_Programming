# question_url: http://leetcode.com/problems/arithmetic-slices/


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        nums.append(3000)
        stack = []
        count = 0

        for index in range(len(nums) - 1):
            diff = nums[index] - nums[index + 1]
            tuples = [nums[index], nums[index + 1]]
            if diff == 0:
                tuples = [nums[index]]

            if not stack:
                stack.append((diff, set(tuples)))
            else:
                if stack[-1][0] == diff:
                    prev_tuples = stack.pop()[1]
                    if diff != 0:
                        curr_set = set(list(tuples) + list(prev_tuples))
                    else:
                        curr_set = tuples + list(prev_tuples)
                    stack.append((diff, curr_set))
                else:
                    prev = stack.pop()
                    prev_tuples = prev[1]
                    prev_diff = prev[0]
                    if len(prev_tuples) >= 3:
                        length = len(prev_tuples)
                        if prev_diff == 0:
                            length += 1
                        for i in range(3, length + 1):
                            count += length - i + 1
                    stack.append((diff, set(tuples)))

        return count



# approch 

        
# #         approch fails because no means of keeping track of adjcency
#     traverse list 
#     > find the diff bn adjcent nums 
#     > store their diff in dict
#     > when ever you find a diff that already existed and has atleast three tuples mark it / add to output list
    
# #     using stack instead
#     > find the diff bn adjcent nums 
#     > store their diff in stack and the tuples as well

# class Solution:
#   def searchRange(self, nums: list[int], target: int) -> list[int]:
    
#     def find_first_occurrence(nums, target):
#         left, right = 0, len(nums) - 1
#         first_pos = -1
        
#         while left <= right:
#             mid = (left + right) // 2
            
#             if nums[mid] == target:
#                 first_pos = mid
#                 right = mid - 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             else: 
#                 right = mid - 1
                
#         return first_pos

#     def find_last_occurrence(nums, target):
#         left, right = 0, len(nums) - 1
#         last_pos = -1
        
#         while left <= right:
#             mid = (left + right) // 2
            
#             if nums[mid] == target:
#                 last_pos = mid
#                 left = mid + 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             else: 
#                 right = mid - 1
                
#         return last_pos
    
#     first = find_first_occurrence(nums, target)
    
#     if first == -1:
#         return [-1, -1]
        
#     last = find_last_occurrence(nums, target)
    
#     return [first, last]


# solver = Solution()

# my_nums = [5, 7, 7, 8, 8, 10]
# my_target = 8

# result = solver.searchRange(my_nums, my_target)

# print(result)


from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(remaining, combination, start):
            if remaining == 0:
                result.append(list(combination))
                return
            
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                combination.append(candidates[i])
                backtrack(remaining - candidates[i], combination, i + 1)
                combination.pop()

        backtrack(target, [], 0)
        return result

# --- Main execution block to run and test the solution ---
if __name__ == '__main__':
    # Create an instance of the Solution class
    solver = Solution()

    # --- Example 1 ---
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    print(f"Candidates: {candidates1}, Target: {target1}")
    solution1 = solver.combinationSum2(candidates1, target1)
    print(f"Output: {solution1}")
    # Expected Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    print("-" * 20)

    # --- Example 2 ---
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    print(f"Candidates: {candidates2}, Target: {target2}")
    solution2 = solver.combinationSum2(candidates2, target2)
    print(f"Output: {solution2}")
    # Expected Output: [[1, 2, 2], [5]]
    print("-" * 20)

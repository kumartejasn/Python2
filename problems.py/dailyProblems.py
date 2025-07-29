class Solution:
  def searchRange(self, nums: list[int], target: int) -> list[int]:
    
    def find_first_occurrence(nums, target):
        left, right = 0, len(nums) - 1
        first_pos = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                first_pos = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else: 
                right = mid - 1
                
        return first_pos

    def find_last_occurrence(nums, target):
        left, right = 0, len(nums) - 1
        last_pos = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                last_pos = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else: 
                right = mid - 1
                
        return last_pos
    
    first = find_first_occurrence(nums, target)
    
    if first == -1:
        return [-1, -1]
        
    last = find_last_occurrence(nums, target)
    
    return [first, last]


solver = Solution()

my_nums = [5, 7, 7, 8, 8, 10]
my_target = 8

result = solver.searchRange(my_nums, my_target)

print(result)
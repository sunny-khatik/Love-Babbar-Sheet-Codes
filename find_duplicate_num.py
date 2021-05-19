# https://leetcode.com/problems/find-the-duplicate-number/submissions/
# without changing array using tortoise method aka floyd cycle detection
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow=nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow!= fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow

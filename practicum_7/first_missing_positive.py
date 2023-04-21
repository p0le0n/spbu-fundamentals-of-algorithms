import typing

class Solution(object):

    def firstMissingPositive(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """

        if 1 not in nums:
            return 1

        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i] = nums[0]
                nums[0] = 1
                break
        for i in range(1, len(nums)):
            if nums[i] == nums[0] + 1:
                nums[0] += 1
        return nums[0] + 1





if __name__ == "__main__":
    # Let's solve First Missing Positive problem:
    # https://leetcode.com/problems/first-missing-positive
    sol = Solution()
    nums = [0, 1, 2]
    n = sol.firstMissingPositive(nums)
    print(n)
    nums = [2, 1]
    n = sol.firstMissingPositive(nums)
    print(n)
    nums = [1, 2, 0]
    n = sol.firstMissingPositive(nums)
    print(n)
    nums = [3, 4, -1, 1]
    n = sol.firstMissingPositive(nums)
    print(n)
    nums = [7, 8, 9, 11, 12]
    n = sol.firstMissingPositive(nums)
    print(n)
    nums = [-5, 0, 1, 7, 10]
    n = sol.firstMissingPositive(nums)
    print(n)
    nums = [1, 0, 15, -8, 7, 2, 3]
    n = sol.firstMissingPositive(nums)
    print(n)


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        def binary_search(left, right):

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        results = binary_search(0, pivot - 1)
        if results != -1:
            return results

        return binary_search(pivot, len(nums) - 1)

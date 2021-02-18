from typing import List


class Solution:
    """
    Runtime: 88 ms, faster than 85.39% of Python3 online submissions for Median of Two Sorted Arrays.
    Memory Usage: 14.2 MB, less than 99.34% of Python3 online submissions for Median of Two Sorted Arrays.
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        half = int(len(merged) / 2)
        if half != len(merged) / 2:
            return merged[half]
        return (merged[half - 1] + merged[half]) / 2


if __name__ == '__main__':
    print("Input: {} {}".format([1, 3], [2]))
    response = Solution().findMedianSortedArrays([1, 3], [2])
    print("Output: {}".format(response))

    print("Input: {} {}".format([1, 2], [3, 4]))
    response = Solution().findMedianSortedArrays([1, 2], [3, 4])
    print("Output: {}".format(response))

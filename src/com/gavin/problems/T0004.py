# 4. Median of Two Sorted Arrays
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)

        if len1 > len2:
            len1, len2, a, b = len2, len1, nums2, nums1
        else:
            a, b = nums1, nums2
        kmin, kmax, median_index = 0, len1, (len1 + len2 + 1) / 2
        while kmin <= kmax:
            k = (kmin + kmax) / 2
            m = median_index - k
            if k < len1 and a[k] < b[m-1]:
                kmin += 1
            elif k > 0 and a[k - 1] > b[m]:
                kmax -= 1
            else:
                if k == 0:
                    left = b[m - 1]
                else:
                    left = b[m - 1] if m > 0 and b[m - 1] > a[k - 1] else a[k - 1]

                if (len1 + len2) % 2 != 0:
                    return left

                if k == len1:
                    right = b[m]
                else:
                    right = b[m] if m < len2 and b[m] < a[k] else a[k]
                return (left + right) / 2.0


s = Solution()
nums1 = [3,4]
nums2 = [1,2]
print(s.findMedianSortedArrays(nums1, nums2))

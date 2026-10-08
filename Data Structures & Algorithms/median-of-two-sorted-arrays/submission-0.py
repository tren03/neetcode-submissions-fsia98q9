class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m < n:
            b,a = nums1, nums2
        else:
            b,a = nums2, nums1


        l = 0
        r = len(b) - 1
        total = m+n
        total_left = (m+n)//2
        while True:
            # these are indexes
            b_boundary = (l+r)//2
            a_boundary = (total_left) - (b_boundary+1) - 1

            b_left = float('-inf') if b_boundary < 0 else b[b_boundary]
            b_right = float('inf') if b_boundary+1 >= len(b) else b[b_boundary+1]
            a_left = float('-inf') if a_boundary < 0 else a[a_boundary]
            a_right = float('inf') if a_boundary+1 >= len(a) else a[a_boundary+1]

            if b_left <= a_right and a_left <= b_right:
                # this is our answer
                if total % 2 != 0:
                    return float(min(a_right, b_right))
                return float(min(b_right, a_right) + max(b_left, a_left)) / 2
            elif b_left > a_right:
                # b has too much, reduce
                r = b_boundary - 1
            else:
                l = b_boundary + 1



        
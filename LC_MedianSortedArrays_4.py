def findMedianSortedArrays(nums1, nums2):
        def fun(i, j, k):
            if i >= a:
                return nums2[j + k - 1]
            if j >= b:
                return nums1[i + k - 1]
            if k == 1:
                return min(nums1[i], nums2[j])

            p = k // 2
            m = nums1[i + p - 1] if i + p - 1 < a else float('inf')
            n = nums2[j + p - 1] if j + p - 1 < b else float('inf')

            if m < n:
                return fun(i + p, j, k - p)
            else:
                return fun(i, j + p, k - p)

        a, b = len(nums1), len(nums2)
        total = a + b

        if total % 2 == 1:
            return fun(0, 0, total // 2 + 1)
        else:
            left = fun(0, 0, total // 2)
            right = fun(0, 0, total // 2 + 1)
            return (left + right) / 2

#main
nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))
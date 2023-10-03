def merge(nums1, nums2, m, n):
    k, j = 0, 0


    while (m != 0 and nums1[-1] == 0):
        nums1.pop()

    while (k < m and j < n):
        while (k + 1 < m and nums1[k] > nums1[k + 1] and nums1[k+1]!=0):
            nums1[k], nums1[k + 1] = nums1[k + 1], nums1[k]
            k += 1
        if nums1[k] < nums2[j]:
            k += 1
        elif (nums1[k] == nums2[j]):
            nums1.insert(k, nums2[j])
            k += 1
            j += 1
        else:
            nums1.insert(k, nums2[j])
            k += 1
            j += 1
        # print(k)

    while (j < n):
        if (nums1[k] > nums2[j]):
            nums1.insert(k , nums2[j])
            j += 1
        else:
            nums1.extend(nums2[j:])
            break


    while (nums1[0] == 0):
        nums1.pop(0)
    return nums1

numb = merge([4,0,0,0,0,0], [1,2,3,5,6], 1, 5)
print(numb)
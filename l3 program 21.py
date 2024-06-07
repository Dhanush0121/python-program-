
nums = [3, 4, 5, 1, 2]
left = 0
right = len(nums) - 1
while left < right:
    mid = left + (right - left) // 2
    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid
min_element = nums[left]
print(min_element)

例子：找第一个 >= target 的位置

def lower_bound(nums, target):
    left = 0
    right = len(nums)
    while  left <= right:
        mid = (left + right) // 2
        if mid >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
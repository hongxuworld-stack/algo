# ou are given a sorted array of digits `array` and an integer `target`.

# Each digit in `array` is between 0 and 9.

# You may use each digit any number of times.

# Your task is to return the largest integer that can be formed using only digits from `array`, such that the integer is less than or equal to `target`.

# If no valid positive number can be formed, return 0.

# Example 1:
# Input: array = [4, 5, 8], target = 878
# Output: 858

# Example 2:
# Input: array = [4, 5, 8], target = 843
# Output: 588

# Example 3:
# Input: array = [4, 5, 8], target = 443
# Output: 88

# Example 4:
# Input: array = [3, 4, 5, 8], target = 442
# Output: 438

def findLargest(arr, target):
    s = str(target)
    max_digit = arr[-1]

    res = []

    for i, ch in enumerate(s):
        cur = int(ch)

        # 找 <= cur 的最大数字
        candidate = None
        for d in arr:
            if d <= cur:
                candidate = d
            else:
                break

        if candidate is not None:
            res.append(candidate)

            # 如果 candidate < cur，后面可以全部填最大数字
            if candidate < cur:
                res += [max_digit] * (len(s) - i - 1)
                return int("".join(map(str, res)))

        else:
            # 当前位没有数字能放，需要回退
            while res:
                last = res.pop()

                # 找比 last 小的最大数字
                smaller = None
                for d in arr:
                    if d < last:
                        smaller = d
                    else:
                        break

                if smaller is not None:
                    res.append(smaller)
                    res += [max_digit] * (len(s) - len(res))
                    return int("".join(map(str, res)))

            # 如果第一位都无法放，只能用更短长度
            if len(s) == 1:
                return 0

            return int(str(max_digit) * (len(s) - 1))

    return int("".join(map(str, res)))
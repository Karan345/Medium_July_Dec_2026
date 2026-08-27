def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left + 1, right + 1]  # 1-indexed output
        elif curr_sum < target:
            left += 1  # Need larger sum -> move left rightward
        else:
            right -= 1 # Need smaller sum -> move right leftward
    return []
# partitioning the array into two parts, one with unique elements and the other with duplicates

def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]  # Overwrite duplicate
    return slow + 1  # Length of unique subarray
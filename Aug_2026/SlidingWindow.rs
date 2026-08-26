pub fn two_sum_sorted(numbers: &[i32], target: i32) -> Vec<i32> {
    let mut left: usize = 0;
    let mut right: usize = numbers.len() - 1;

    while left < right {
        let current_sum = numbers[left] + numbers[right];

        if current_sum == target {
            return vec![(left + 1) as i32, (right + 1) as i32];
        } else if current_sum < target {
            left += 1;
        } else {
            right -= 1;
        }
    }
    vec![]
}

pub fn remove_duplicates(nums: &mut Vec<i32>) -> usize {
    if nums.is_empty() {
        return 0;
    }

    let mut slow: usize = 0;

    for fast in 1..nums.len() {
        if nums[fast] != nums[slow] {
            slow += 1;
            nums[slow] = nums[fast];
        }
    }

    slow + 1
}
/// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

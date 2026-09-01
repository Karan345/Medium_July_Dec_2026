pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
    let s_bytes = s.as_bytes();
    let p_bytes = p.as_bytes();
    let p_len = p_bytes.len();
    let s_len = s_bytes.len();

    if p_len > s_len {
        return vec![];
    }

    let mut p_count = [0i32; 26];
    let mut window_count = [0i32; 26];
    let mut result = Vec::new();

    // Populate initial frequencies for p and the first window of s
    for i in 0..p_len {
        p_count[(p_bytes[i] - b'a') as usize] += 1;
        window_count[(s_bytes[i] - b'a') as usize] += 1;
    }

    // Check if initial window is a match
    if p_count == window_count {
        result.push(0);
    }

    // Slide window across remainder of s
    for right in p_len..s_len {
        // Add incoming character on the right
        window_count[(s_bytes[right] - b'a') as usize] += 1;
        
        // Remove outgoing character on the left
        let left_out = right - p_len;
        window_count[(s_bytes[left_out] - b'a') as usize] -= 1;

        // Compare frequency states (O(1) comparison for fixed array size 26)
        if window_count == p_count {
            result.push((left_out + 1) as i32);
        }
    }

    result
}
import time

def longest_substring_brute_force(s: str):
    n = len(s)
    max_len = 0
    max_substr = ""
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if len(set(substring)) == len(substring):
                if len(substring) > max_len:
                    max_len = len(substring)
                    max_substr = substring
    return max_substr, max_len

def longest_substring_sliding_window(s: str):
    n = len(s)
    char_set = set()
    left = 0
    max_len = 0
    max_substr = ""
    
    for right in range(n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        
        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_substr = s[left:right + 1]
    
    return max_substr, max_len

input_string = "abcabcbb"

start_time = time.time()
brute_force_result = longest_substring_brute_force(input_string)
end_time = time.time()
brute_force_time = end_time - start_time

start_time = time.time()
sliding_window_result = longest_substring_sliding_window(input_string)
end_time = time.time()
sliding_window_time = end_time - start_time

print("Brute Force Result: ", brute_force_result)
print("Brute Force Execution Time: ", brute_force_time)
print("Sliding Window Result: ", sliding_window_result)
print("Sliding Window Execution Time: ", sliding_window_time)

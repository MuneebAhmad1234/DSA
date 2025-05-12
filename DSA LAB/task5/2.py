def are_anagrams(str1, str2):
    """
    Function to determine whether two strings are anagrams using a hash table (dictionary).
    """
    if len(str1) != len(str2):
        return False

    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return all(count == 0 for count in char_count.values())


print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False
print(are_anagrams("triangle", "integral"))  # Output: True
print(are_anagrams("aabbcc", "ccbbaa"))  # Output: True
print(are_anagrams("abcd", "abcde"))     # Output: False

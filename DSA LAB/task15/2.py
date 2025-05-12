def permute(string):
    def backtrack(start):
        if start == len(chars):
            result.append(''.join(chars))
            return
        seen = set()
        for i in range(start, len(chars)):
            if chars[i] in seen:
                continue
            seen.add(chars[i])
            chars[start], chars[i] = chars[i], chars[start]
            backtrack(start + 1)
            chars[start], chars[i] = chars[i], chars[start]

    chars = list(string)
    result = []
    backtrack(0)
    return result

# Example usage
print(permute("ABC"))  # Expected Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return all(count == 0 for count in char_count.values())

test_cases = [
    ("listen", "silent"),
    ("triangle", "integral"),
    ("apple", "pale"),
    ("rat", "car"),
]

for str1, str2 in test_cases:
    print(f"Are '{str1}' and '{str2}' anagrams? {are_anagrams(str1, str2)}")

class SimpleCache:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key, None)

    def set(self, key, value):
        self.cache[key] = value

    def has_key(self, key):
        return key in self.cache

cache = SimpleCache()
cache.set("name", "GitHub Copilot")
print(cache.get("name"))
print(cache.has_key("name"))
print(cache.has_key("age"))

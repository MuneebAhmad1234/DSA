import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_counter = Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in freq_counter.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

def generate_huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}
    if root is None:
        return codes
    if root.char is not None:
        codes[root.char] = current_code
    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)
    return codes

def huffman_encoding(text):
    if not text:
        return {}, ""
    root = build_huffman_tree(text)
    huffman_codes = generate_huffman_codes(root)
    encoded_text = ''.join(huffman_codes[char] for char in text)
    return huffman_codes, encoded_text

def compare_data_sizes(text, encoded_text):
    original_size = len(text) * 8
    compressed_size = len(encoded_text)
    return original_size, compressed_size

if __name__ == "__main__":
    text = "hello greedy"
    huffman_codes, encoded_text = huffman_encoding(text)
    print("Huffman Codes:", huffman_codes)
    print("Encoded Text:", encoded_text)
    original_size, compressed_size = compare_data_sizes(text, encoded_text)
    print(f"Original Size: {original_size} bits")
    print(f"Compressed Size: {compressed_size} bits")
    print("\nExplanation:")
    print("Huffman Coding is a greedy algorithm because it builds the tree by repeatedly merging the two smallest frequency nodes. This ensures that the most frequent characters get the shortest codes, minimizing the average code length.")

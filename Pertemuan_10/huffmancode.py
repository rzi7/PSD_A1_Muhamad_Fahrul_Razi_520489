import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, frequency, symbol, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right
        
    def __lt__(self, other):
        return self.frequency < other.frequency

def huffman_tree(data):
    # Menghitung frekuensi tiap karakter
    frequency = Counter(data)
    
    # Buat antrian prioritas untuk menampung node
    heap = [HuffmanNode(freq, char) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        # Ekstrak dua node dengan frekuensi terendah
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Buat node baru dengan dua node ini sebagai anak
        merged = HuffmanNode(left.frequency + right.frequency, left.symbol + right.symbol, left, right)
        
        # Tambahkan node baru ke heap
        heapq.heappush(heap, merged)
    
    # Node yang tersisa adalah akar dari pohon Huffman
    return heap[0]

def huffman_codes(node, current_code="", codes={}):
    if node is None:
        return
    
    # Jika simpulnya adalah simpul daun, maka simpul tersebut berisi simbol
    if not node.left and not node.right:
        codes[node.symbol] = current_code
    
    # Lintasi anak kiri dan kanan
    huffman_codes(node.left, current_code + "0", codes)
    huffman_codes(node.right, current_code + "1", codes)
    
    return codes

def decode_huffman(root, encoded_data):
    decoded_data = ""
    current_node = root
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        # Jika kita mencapai leaf node, tambahkan simbol ke hasilnya
        if not current_node.left and not current_node.right:
            decoded_data += current_node.symbol
            current_node = root
    
    return decoded_data

def main():
    # Membaca data masukan dari pengguna
    data = input("Masukkan kata atau kalimat yang ingin di kompresi: ")
    
    # Membuat Huffman tree
    root = huffman_tree(data)
    
    # Generate Huffman codes
    codes = huffman_codes(root)
    
    print("Huffman Codes:")
    for char in codes:
        print(f"{char}: {codes[char]}")
    
    # Encode the data
    encoded_data = ''.join([codes[char] for char in data])
    print(f"Hasil Encode Data: {encoded_data}")
    
    # Decode the data
    decoded_data = decode_huffman(root, encoded_data)
    print(f"Data Yang Di Kompres Data: {decoded_data}")

if __name__ == "__main__":
    main()

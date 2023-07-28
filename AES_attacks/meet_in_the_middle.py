from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def meet_in_the_middle_attack(ciphertext):
    # Known plaintext-ciphertext pair
    known_plaintext = b"Hello, "
    known_ciphertext = b"\x1c\x64\x3f\x11\x19\xf2\x95\x78\x30\x8e\x0c\x9d\x99\xec\x21\x55"
    # Iterate over all possible key combinations
    for i in range(256):
        for j in range(256):
            # Generate potential keys for encryption and decryption
            key1 = bytes([i] * 16) # First key for encryption
            key2 = bytes([j] * 16) # Second key for decryption
            # Create AES cipher objects with the potential keys
            cipher1 = AES.new(key1, AES.MODE_ECB)
            cipher2 = AES.new(key2, AES.MODE_ECB)
            # Encrypt known plaintext with first key and decrypt the known ciphertext with the second key
            intermediate = cipher1.encrypt(pad(known_plaintext, AES.block_size))
            decrypted = cipher2.decrypt(ciphertext)
            # Check if the intermediate result matches the decrypted result
            if intermediate == decrypted:
                print("Potential Keys Found:")
                print("Key1:", key1.hex())
                print("Key2:", key2.hex())
                return key1, key2
    print("No potential keys found.")
    return None, None

# Example usage
ciphertext = b"\x1c\x64\x3f\x11\x19\xf2\x95\x78\x30\x8e\x0c\x9d\x99\xec\x21\x55"
meet_in_the_middle_attack(ciphertext)
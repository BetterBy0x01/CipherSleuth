from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def brute_force_aes(ciphertext):
    # Set the known plaintext
    plaintext = b"Hello, world!"
    # Iterate over all possible keys
    for key_candidate in generate_keys():
        try:
            # Create an AES cipher object with the key candidate
            cipher = AES.new(key_candidate, AES.MODE_ECB)
            # Decrypt the ciphertext using the key candidate
            decrypted = cipher.decrypt(ciphertext)
            # Check if the decrypted plaintext matches the known plaintext
            if decrypted == pad(plaintext, AES.block_size):
                print("Key found:", key_candidate.hex())
                return key_candidate
        except ValueError:
            # Incorrect padding or decryption error, continue to the next key
            continue
    print("Key not found.")
    return None

def generate_keys():
    # This is a simplified example
    # In reality, you would need to iterate over the entire key space
    for i in range(256):
        yield bytes([i] * 16) # Assuming AES-128

# Example usage
ciphertext = b"\x82\x0f\x4a\xdc\xaf\x4d\xee\xdb\xae\x32\x5d\xcd\x33\xef\x73\x46"
brute_force_aes(ciphertext)
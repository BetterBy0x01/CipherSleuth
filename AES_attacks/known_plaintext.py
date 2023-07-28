from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def known_plaintext_attack(plaintext, ciphertext):
    # Iterate over all possible keys
    for key_candidate in generate_keys():
        try:
            # Create an AES cipher object with the key candidate
            cipher = AES.new(key_candidate, AES.MODE_ECB)
            # Encrypt the plaintext using the key candidate
            encrypted = cipher.encrypt(pad(plaintext, AES.block_size))
            # Check if the encrypted ciphertext matches the known ciphertext
            if encrypted == ciphertext:
                print("Key found:", key_candidate.hex())
            return key_candidate

        except ValueError:
        # Incorrect padding or encryption error, continue to the next key
            continue
    return None
def generate_keys():
    # This is a simplified example
    # In reality, you would need to iterate over the entire key space
    for i in range(256):
        yield bytes([i] * 16) # Assuming AES-128

# Example usage
plaintext = b"Hello, world!"
ciphertext = b"\x82\x0f\x4a\xdc\xaf\x4d\xee\xdb\xae\x32\x5d\xcd\x33\xef\x73\x46"
key = known_plaintext_attack(plaintext, ciphertext)
if (key == None):
    print("Key Not Found")
else:
    print(f"Key: {key}")
import banner
import vigenere
import railFence

banner.banner()

print(banner.blue + "[1] Vigenere Cipher\n" + banner.reset
    +banner.yellow + "[2] Rail Fence\n" + banner.reset
    +banner.green + "[3] Exit\n" + banner.reset
    )
choice = int(input(banner.blue + ">> " + banner.reset))

# Vigenere
if choice == 1:
    encryptedText = input(banner.blue + ">> EncryptedText = " + banner.reset)
    key = input(banner.blue + ">> key = " + banner.reset)
    decryptedText = vigenere.vigenere_decrypt(encryptedText, key)
    print(banner.yellow + f"Decrypted Text: {decryptedText}\n" + banner.reset)

# Rail Fence
if choice == 2:
    encryptedText = input(banner.blue + ">> EncryptedText = " + banner.reset)
    rails = int(input(banner.blue + ">> rails = " + banner.reset))
    decryptedText = railFence.rail_fence_decrypt(encryptedText, rails)
    print(banner.yellow + f"Decrypted Text: {decryptedText}\n" + banner.reset)
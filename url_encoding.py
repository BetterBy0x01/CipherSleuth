import banner
import urllib.parse

banner.banner()

print(banner.blue + "[1] Encode URL\n" + banner.reset
    +banner.yellow + "[2] Decode URL\n" + banner.reset
    +banner.green + "[3] Exit\n" + banner.reset
    )
choice = int(input(banner.blue + ">> " + banner.reset))

# Encode URL
if choice == 1:
    url = input(banner.blue + ">> Enter the URL: " + banner.reset)
    encoded_url = urllib.parse.quote(url)
    print(banner.red + "\n[+] Please Wait...\n" + banner.reset)
    print(banner.yellow + f"Encoded URL: {encoded_url}\n" + banner.reset)

# Decode URL
if choice == 2:
    url = input(banner.blue + ">> Enter the encoded URL: " + banner.reset)
    decoded_url = urllib.parse.quote(url)
    print(banner.red + "\n[+] Please Wait...\n" + banner.reset)
    print(banner.yellow + f"Decoded URL: {decoded_url}\n" + banner.reset)
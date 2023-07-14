import banner
import binascii
import gmpy2

def Convert(decimal):
    hex_ = hex(decimal).replace("0x", "").replace("L","")
    ascii = binascii.a2b_hex(hex_)
    print("\nPlaintext in Decimal: ", decimal)
    print("Plaintext in Hex: ", hex_)
    print("Plaintext in ascii: ", ascii.decode("utf-8") + "\n")

def egcd(b, n):
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while n != 0:
        (q, b, n) = (b//n, n, b%n)
        (x0, x1) = (x1, x0-q*x1)
        (y0, y1) = (y1, y0-q*y1)
    return (b, x0, y0)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print(banner.red + "\n[-] Modular Inverse does not exist\n" + banner.reset)
        exit(-1)
    else:
        return x % m


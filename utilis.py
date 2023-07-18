import banner
import binascii
import gmpy2

def Convert(decimal):
    hex_ = hex(decimal).replace("0x", "").replace("L","")
    ascii = binascii.a2b_hex(hex_)
    print("\nPlaintext in Decimal: ", decimal)
    print("Plaintext in Hex: ", hex_)
    print("Plaintext in ascii: ", ascii.decode("utf-8") + "\n")


# Calculating GCD 8:40
# https://youtu.be/yHwneN6zJmU
# EGCD
# https://youtu.be/61sph5R5Juw

def egcd(a, b):
    (s1, s2, t1, t2) = (1, 0, 0, 1)
    while b != 0:
        (q, a, b) = (a//b, b, a%b)
        s = s1 - q*s2
        t = t1 - q*t2
        (s1, s2, t1, t2) = (s2, s, t2, t)
    return a, s1, t1

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print(banner.red + "\n[-] Modular Inverse does not exist\n" + banner.reset)
        exit(-1)
    else:
        return x % m

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# Binary search to find the eth root of a number
def inv_pow(c, e):
    low = -1
    high = c+1
    while (low + 1) < high:
        m = (low + high) // 2                   # OverflowError: interger division result too large for a float
        p = pow(m, e)
        if (p < c):
            low = m
        else:
            high = m
    m = high
    assert pow(m, e) == c
    return m
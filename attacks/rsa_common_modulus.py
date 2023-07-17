# https://infosecwriteups.com/rsa-attacks-common-modulus-7bdb34f331a5
# Different ciphertext & public exponent but same modulus.
import sys
import banner
from utilis import Convert, egcd
from math import gcd
from Crypto.Util.number import inverse

sys.path.append("..")
banner.banner()

# Plaintext is recoverable if gcd(e1, e2)=1 and gcd(ct2, n)=1

def bezout_coefficients(a, b):
    gcd, x, y = egcd(a, b)
    return x, y

try:
    c1 = int(input(banner.blue + ">> c1 = "))
    c2 = int(input(">> c2 = "))
    e1 = int(input(">> e1 = "))
    e2 = int(input(">> e2 = "))
    N = int(input(">> N = " + banner.reset))

    if gcd(e1, e2) != 1:
        raise ValueError("Exponents e1 and e2 must be coprime")

    s1, s2 = bezout_coefficients(e1, e2) 

    temp = inverse(c2, N)
    m1 = pow(c1, s1, N)
    m2 = pow(temp, -s2, N)
    m = (m1*m2)%N
    Convert(m)

except ImportError:
    print(banner.red + "\n[-] Module Not Setup\n" + banner.reset)
except ValueError:
    print(banner.red + "\n[-] e1, e2, n, c1, c2 Must Be Integar Number\n" + banner.reset)
except AssertionError:
    print(banner.red + "\n[-] Wrong Data\n" + banner.reset)
except KeyboardInterrupt:
    exit()
except:
    print(banner.red + "\n[-] False Attack !\n" + banner.reset)
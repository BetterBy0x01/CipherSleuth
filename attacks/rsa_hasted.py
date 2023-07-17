# https://youtu.be/aS57JCzJw_o
import sys
import banner
from utilis import Convert, inv_pow, mul_inv

sys.path.append("..")
banner.banner()

def chinese_remainder_theorem(C, N, e):
    M = 1
    for i in N: 
        M *= i
    m = []
    m_inv = []
    result = 0
    for i in range(e):
        m.append(M // N[i])
        m_inv.append(mul_inv(m[i], N[i]))
        result += (C[i] * m[i] * m_inv[i])
    return (result % M)

try:
    pairsCount = int(input(banner.blue + ">> Number of (n, c) pairs: "))
    N = []
    C = []
    for _ in range(pairsCount):
        n = int(input(banner.blue + ">> n : "))
        c = int(input(">> c : " + banner.reset))
        N.append(n)
        C.append(c)
    e = len(N)
    pe = chinese_remainder_theorem(C, N, e)
    m = inv_pow(pe, e)
    Convert(m)
except ValueError:
    print(banner.red + "\n[-] c1,c2,c3,n1,n2,n3 Must Be Integar Number\n" + banner.reset)
except AssertionError:
    print(banner.red + "\n[-] Wrong Data\n" + banner.reset)
except KeyboardInterrupt:
    exit()

# https://stackoverflow.com/questions/20464561/fermat-factorisation-with-python
# https://youtu.be/tKTNVmnW_4w


# This algorithms works well when p and q are close.

import sys
import banner
import gmpy2

sys.path.append("..")

"""
n = a2 - b2
b2 = a2 - n
b = sqrt(a2 - n)
"""

def factorize(n):
    a = gmpy2.isqrt(n)
    b2 = a*a - n
    b = gmpy2.isqrt(n) 
    while (b*b != b2):
        a = a + 1
        b2 = a*a - n
        b = gmpy2.isqrt(b2)

        # Why this condition?
        if (b > n):
            print(banner.red + "\n[-] Sorry Can't Factorize Number\n" + banner.reset)
            exit()
    p = a+b
    q = a-b
    print(banner.yellow + f'p = {p}')
    print(f'q = {q}\n' + banner.reset)
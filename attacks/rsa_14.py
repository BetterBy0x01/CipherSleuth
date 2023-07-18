# RSA Common Factor
import sys
import banner
from utilis import Convert, modinv, egcd

sys.path.append("..")
banner.banner()

n1 = int(input(banner.blue + ">> n1 = "))
n2 = int(input(">> n2 = "))
c1 = int(input(">> c1 = "))
c2 = int(input(">> c2 = "))
e = int(input(">> e = " + banner.reset))

if egcd(n1, n2)[0] == 1:            # returns gcd
    print(banner.red + "\n[-] Sorry, gcd(n1, n2) = 1\n")
    exit()
else:
    p = egcd(n1, n2)[0]
    q1 = n1 // p
    q2 = n2 // p
    phi1 = (p-1)*(q1-1)
    phi2 = (p-1)*(q2-1)
    d1 = modinv(e, phi1)
    d2 = modinv(e, phi2)
    try:
        m1 = pow(c1, d1, n1)
        Convert(m1)
    except TypeError:               # when a value is not of the expected type.
        pass
    try:
        m2 = pow(c2, d2, n2)
        Convert(m2)
    except TypeError:
        pass

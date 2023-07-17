# https://en.wikipedia.org/wiki/RSA_(cryptosystem)#:~:text=Using%20the%20Chinese%20remainder%20algorithm
import sys
import banner
from utilis import Convert
from Crypto.Util.number import inverse

sys.path.append("..")
banner.banner()

try:
    c = int(input(banner.blue + ">> c = "))
    p = int(input(">> p = "))
    q = int(input(">> q = "))
    dp = int(input(">> dp = "))
    dq = int(input(">> dq = " + banner.reset))

    print(banner.red + "[+] Please Wait ...\n" + banner.reset)

    qinv = inverse(q, p)
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    h = (qinv*(m1-m2)) % p
    m = (m2+(h*q)) % (p*q)
    Convert(m)

except ValueError:
    print(banner.red + "\n[-] c,p,q,dp,dq Must Be Integar Number\n"+ banner.reset)
except AssertionError:
    print(banner.red + "\n[-] Wrong Data\n" + banner.reset)
except KeyboardInterrupt:
    exit()

# https://medium.com/asecuritysite-when-bob-met-alice/in-rsa-we-have-e-d-n-p-and-q-but-what-are-dq-dp-and-invq-79a85fff605a
import sys
import banner
from utilis import modinv, Convert

sys.path.append("..")
banner.banner()

try:
    c = int(input(banner.blue + ">> c = "))
    n = int(input(">> n = "))
    e = int(input(">> e = "))
    dp = int(input(">> dp = " + banner.reset))
    # Bruteforce to get p
    mp = (dp * e) - 1
    for i in range(2, 1000000):
        p = (mp // i) + 1
        if n % p == 0:
            break
    q = n // p
    print(banner.red + "\n[+] Please Wait ..." + banner.reset)
    phi = (p-1)*(q-1)
    d = modinv(e, phi)
    m = pow(c, d, n)
    Convert(m)
except ImportError:
    print(banner.red + "[-] Module Not Setup" + banner.reset)
except ValueError:
    print(banner.red + "[-] c, e, dp, n Must Be Integer Number" + banner.reset)
except KeyboardInterrupt:
    exit()
except:
    print(banner.red + "[-] False Attack" + banner.reset)
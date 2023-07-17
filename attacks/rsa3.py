import sys
import banner
from utilis import modinv, Convert

sys.path.append("..")
banner.banner()

try:
    c = int(input(banner.blue + ">> c = "))
    p = int(input(">> <p or q> = "))
    n = int(input(">> n = "))
    e = int(input(">> e = " + banner.reset))
    q = n // p
    phi = (p-1)*(q-1)
    d = modinv(e, phi)
    m = pow(c, d, n)
    Convert(m)
except ImportError:
    print(banner.red + "[-] Module Not Setup" + banner.reset)
except ValueError:
    print(banner.red + "[-] c, e, <p or q>, n Must Be Integer Number" + banner.reset)
except KeyboardInterrupt:
    exit()
except:
    print(banner.red + "[-] False Attack" + banner.reset)
import sys
import banner
from factorizations.factordb import *
from utilis import modinv, Convert

sys.path.append("..")
banner.banner()

try:
    c = int(input(banner.blue + ">> c = "))
    n = int(input(">> n = "))
    e = int(input(">> e = " + banner.reset))
    factors = factorize(n)
    p = factors[0]
    q = factors[1]
    phi = (p-1)*(q-1)
    d = modinv(e, phi)
    m = pow(c, d, n)
    Convert(m)
except IndexError:
    print(banner.red + "[-] Sorry n Can't Be Factorized")
    print("\n[!] Try to Use Multiple Attack")
except ImportError:
    print(banner.red + "[-] Module Not Setup" + banner.reset)
except ValueError:
    print(banner.red + "[-] c, e, n Must Be Integer Number" + banner.reset)
except KeyboardInterrupt:
    exit()
except:
    print(banner.red + "[-] False Attack" + banner.reset)

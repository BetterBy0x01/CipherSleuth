import sys
import banner
from utilis import Convert, modinv
from factorizations.ecm import primefactors

sys.path.append("..")
banner.banner()

try:

    c = int(input(banner.blue + ">> c = "))
    n = int(input(">> n = "))
    e = int(input(">> e = " + banner.reset))
    prime = primefactors(n)

    phi = 1
    for i in prime:
        phi *= i-1

    d = modinv(e, phi)
    m = pow(c, d, n)
    Convert(m)

except IndexError:
    print(banner.red + "[-] Sorry Can't Factorize n " + banner.reset)
except ImportError:
    print(banner.red + "\n[-] Module Not Setup" + banner.reset)
except ValueError:
    print(banner.red + "\n[-] c,n,e Must Be Integar Number" + banner.reset)
except KeyboardInterrupt:
    exit()
except:
    print(banner.red + "[-] False Attack !" + banner.reset)

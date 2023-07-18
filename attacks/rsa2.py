import sys
import banner
from utilis import Convert, modinv

# Add the parent directory to the sys.path list
sys.path.append("..")

banner.banner()

try:
    c = int(input(banner.blue + ">> c = " + banner.reset))
    p = int(input(">> p = "))
    q = int(input(">> q = "))
    e = int(input(">> e = " + banner.reset))

    n = p*q
    phi = (p-1)*(q-1)
    d = modinv(e, phi)
    m = pow(c, d, n)
    Convert(m)
except ImportError:
    print("\n[-] Module Not Setup")
except ValueError:
    print(banner.red + "\n[-] c, p, q, e Must Be Integer Number\n"+ banner.reset)
except AssertionError:
    print("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
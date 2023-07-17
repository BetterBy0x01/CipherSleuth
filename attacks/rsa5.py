import sys
import banner
from utilis import Convert

sys.path.append("..")
banner.banner()


# TO-DO: Check if phi & n have the same p & q vlaues

try:
    c = int(input(banner.blue + ">> c = "))
    n = int(input(">> n = "))
    d = int(input(">> d = "))
    e = int(input(">> e = "))
    phi = int(input(">> phi = " + banner.reset))
    m = pow(c, d, n)
    Convert(m)
except ImportError:
    print(banner.red + "[-] Module Not Setup" + banner.reset)
except ValueError:
    print(banner.red + "[-] c, d, e, phi, n Must Be Integer Number" + banner.reset)
except KeyboardInterrupt:
    exit()
except:
    print(banner.red + "[-] False Attack" + banner.reset)
import sys
import banner
from utilis import Convert

sys.path.append("..")
banner.banner()

try:
    c = int(input(banner.blue + ">> c = "))
    n = int(input(">> n = "))
    d = int(input(">> d = " + banner.reset))
    m = pow(c,d,n)
    Convert(m)
except ValueError:
    print(banner.red + "\n[-] c,n,d Must Be Integar Number\n" + banner.reset)
except AssertionError:
    print(banner.red + "\n[-] Wrong Data\n" + banner.reset)
except KeyboardInterrupt:
    exit()
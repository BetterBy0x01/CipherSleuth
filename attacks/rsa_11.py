import sys
import banner
from utilis import Convert, egcd
from math import gcd
from Crypto.Util.number import inverse

sys.path.append("..")
banner.banner()

def premRSA():
    pass

try:
    c = int(input(">>> c = "))
    n = int(input(">>> n = "))
    e = int(input(">>> e = "))
    d = int(input(">>> d = "))
    m = premRSA(n,e,d,c)
    Convert(m)

except ValueError:
    print(banner.red + "\n[-] c,n,d,e Must Be Integar Number\n" + banner.reset)
except AssertionError:
    print(banner.red + "\n[-] Wrong Data\n" + banner.reset)
except KeyboardInterrupt:
    exit()
except:
    print(banner.red + "\n[-] False Attack !\n" + banner.reset)
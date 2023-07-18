import sys
import banner
from utilis import Convert

sys.path.append("..")
banner.banner()

try:
    import gmpy2
    c = int(input(banner.blue + ">> c = " + banner.reset))
    m = gmpy2.iroot(c, 3)[0]
    assert pow(m,3) == c
    Convert(m)
except ImportError:
    print(banner.red + "\n[-] Module Not Setup" + banner.reset)
except ValueError:
    print(banner.red + "\n[-] c Must Be Integar Number" + banner.reset)
except AssertionError:
    print(banner.red + "\n[-] Wrong Data" + banner.reset)
except KeyboardInterrupt:
    exit()
except:
    print(banner.red + "\n[-] False Attack !" + banner.reset)

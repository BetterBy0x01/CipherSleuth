# https://youtu.be/OpPrrndyYNU
import sys
import banner
from utilis import Convert, egcd
from math import gcd
from Crypto.Util.number import inverse

sys.path.append("..")
banner.banner()

try:
    n = int(banner.blue + ">> n = ")
    e = int(">> e = " + banner.reset)
    
except ImportError:
    print(banner.red + "\n[-] Module Not Setup\n" + banner.reset)
except ValueError:
    print(banner.red + "\n[-] c,p,q,e Must Be Integar Number\n" + banner.reset)
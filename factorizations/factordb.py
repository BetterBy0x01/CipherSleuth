from factordb.factordb import FactorDB
import banner
import requests
def factorize(n):
    try:
        f = FactorDB(n)
        f.connect()
        return f.get_factor_list()
    except requests.exceptions.ConnectionError:
        print(banner.red + "\n[-] Check Your Internet" + banner.reset)
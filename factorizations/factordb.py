from factordb.factordb import FactorDB
def factorize(n):
    f = FactorDB(n)
    f.connect()
    return f.get_factor_list()
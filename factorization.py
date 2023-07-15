import banner
import factorizations.factordb as factordb
import factorizations.fermat as fermat
import factorizations.ecm as ecm
import factorizations.qs as qs

banner.banner()

print(banner.blue + "[1] FactorDB Factorization\n" + banner.reset
    +banner.yellow + "[2] Fermat Factorization\n" + banner.reset
    +banner.red + "[3] ECM Factorization\n" + banner.reset
    +banner.violet + "[4] Quadratic Sieve Factorization\n" + banner.reset
    +banner.green + "[5] Exit\n" + banner.reset
    )
choice = int(input(banner.blue + ">> " + banner.reset))

# FactorDB
if choice == 1:
    n = int(input(banner.blue + ">> n = " + banner.reset))
    print(banner.red + "\n[+] Please Wait...\n" + banner.reset)
    print(banner.yellow + f"Primes: {factordb.factorize(n)}\n" + banner.reset)

# Fermat
if choice == 2:
    n = int(input(banner.blue + ">> n = " + banner.reset))
    print(banner.red + "\n[+] Please Wait...\n" + banner.reset)
    fermat.factorize(n)
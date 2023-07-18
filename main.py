import banner
import os

banner.banner()

print(banner.yellow + """
[1] RSA Attacks
[2] Factorize Number
"""
    + banner.reset
)

choice = int(input(banner.blue + ">> " + banner.reset))
os.system("clear")
if (choice == 2):
    import factorization
elif (choice == 1):
    banner.banner()
    print(banner.yellow + """
[1]  Attack(c, n, e)
[2]  Attack(c, p, q, e)
[3]  Attack(c, n, e, {p or q})
[4]  Attack(c, n, e, dp)
[5]  Attack(c, n, d, e, phi)
[6]  Attack(c1, c2, c3, n1, n2, n3, e=3)         [Hasted]
[7]  Attack(c1, c2, e1, e2, n)                   [Common Modulus]
[8]  Attack(c, p, q, dp, dq)                     [Chinese Remainder Theorem]
[9]  Attack(n, e)                                [Wiener]
[10] Attack(c, n, d)
[11] Attack(c, d, n, e)
[12] Attack(c, n, e)                             [Multi Prime Number]
[13] Attack(c, e = 3)                            
[14] Attack(c1, c2, n1, n2, e)                   [Common Factor]
[0] Exit
    """ + banner.reset)
    option = int(input(banner.blue + ">> " + banner.reset))
    if (1 <= option <= 14):
        os.system("clear")
    if (option == 1):
        import attacks.rsa
    elif (option == 2):
        import attacks.rsa2
    elif (option == 3):
        import attacks.rsa3
    elif (option == 4):
        import attacks.rsa4
    elif (option == 5):
        import attacks.rsa5
    elif (option == 6):
        import attacks.rsa_hasted
    elif (option == 7):
        import attacks.rsa_common_modulus
    elif (option == 8):
        import attacks.rsa_chinese_remainder_theorem
    elif (option == 9):
        import attacks.rsa_wiener
    elif (option == 10):
        import attacks.rsa_10
    elif (option == 11):
        import attacks.rsa_11
    elif (option == 12):
        import attacks.rsa_multi_prime
    elif (option == 13):
        import attacks.rsa_13
    elif (option == 14):
        import attacks.rsa_14
    else:
        exit()
else:
    exit()

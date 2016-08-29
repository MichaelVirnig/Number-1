# Michael Virnig
# Diffie Hellman Key Exchange

def invmod(p, q):
    m = q; d0 = q; d1 = p; x0 = 0; x1 = 1
    while d1 != 0:
        q = int(d0/d1)
        d2 = (d0-(q*d1))
        x2 = (x0-(q*x1))
        x0 = x1; x1 = x2; d0 = d1; d1 = d2
    mod1 = int(x0%m)
    return mod1

def gcd(a, b):
    n = a; m = b
    while n != 0:
        n, m = m%n, n
    if m == 1:
        return 1
    else:
        return 0

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n < 9:
        return True
    if n%3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0:
            return False
        if n%(f+2) == 0:
            return False
        f +=6
    return True

def MENU():
    while True:
        try:
            menu = eval(input("\nPlease select from the following choices:\n"
                         "\n\t1) Start as Alice\n"
                         "\n\t2) Start as Bob\n"
                         "\n\t3) Exit the program\n"
                         "\nEnter your choice (1 || 2 || 3): "))
            if (1 <= menu <= 3):
                print("\n"*60)
                return menu
                break
            else:
                raise
        except:
            print("\n"*60)
            print("\nThat is not a valid selection, try again.\n")
    
def main():
    menu = 0
    while menu != 3:
        menu = MENU()
        try:
                if menu == 1:
                    print("\nWelcome to my Diffie Hellman Key Exchange program!\n")
                    print("You may enter Control+C at anytime to bring up the main menu.\n\n")
                    print("You have chosen to start communication as Alice.\n")
                    sharedPrime = eval(input("Please enter the agreed upon prime number: "))
                    Pcheck = isPrime(sharedPrime)
                    if(Pcheck == True):
                        phi = sharedPrime - 1
                        print("\nBased on ", sharedPrime, ", Phi is ", phi)
                    else:
                        print("\n"*50)
                        print(sharedPrime, " is not a prime number, please try again.\n")
                        
                    AliceKey = eval(input("\nPlease enter Alice's Private Key: \t"))
                    primecheck = gcd(AliceKey, phi)
                    if(primecheck == 0):
                        print("\n"*50)
                        print("Alice's private key is not relatively prime to phi, please choose again.\n")
                        raise
                    else:
                        Amodphi = invmod(AliceKey, phi)
                        print("\nAlice computes ", AliceKey, "^-1 mod",phi)
                        print("\nThe inverse mod of the private key is ", Amodphi)
                    BobKey = eval(input("\nPlease enter Bob's Private key: \t"))
                    primecheck = gcd(BobKey, phi)
                    if(primecheck == 0):
                        print("\n"*50)
                        print("Bob's private key is not relatively prime to phi, please choose again.\n")
                        raise
                    else:
                        Bmodphi = invmod(BobKey, phi)
                        print("\nBob computes ", BobKey, "^-1 mod",phi)
                        print("\nThe inverse mod of the private key is ", Bmodphi)
                    k = eval(input("\nEnter your Secret Key(k) Value: \t"))
                    if k >= phi:
                        print("\nYour Secret Key must be less than the Shared Prime minus 1.")
                        print("\nPlease try again.")
                        raise
                    k1 = (k**AliceKey % sharedPrime)
                    print("\n\nAlice computes ", k,"^",AliceKey,"mod", sharedPrime, "=", k1)
                    print("\nAlice sends ", k1, " to Bob ---------------->\n")
                    k2 = (k1**BobKey % sharedPrime)
                    print("\n\t\t\tBob computes ", k1,"^",BobKey,"mod", sharedPrime, "=", k2)
                    print("\n\t             <---------------- Bob sends ", k2, " to Alice\n")
                    k3 = (k2**Amodphi % sharedPrime)
                    print("\nAlice computes ", k2,"^",Amodphi,"mod", sharedPrime, "=", k3)
                    print("\nAlice sends ", k3, " to Bob ---------------->\n")
                    k4 = (k3**Bmodphi % sharedPrime)
                    print("\n\t\t\tBob computes ", k3,"^",Bmodphi,"mod", sharedPrime, "=", k4)
                    print("\n\t\t\tBob now has the shared secret key!", k4,"\n")
                if menu == 2:
                    print("\nWelcome to my Diffie Hellman Key Exchange program!\n")
                    print("You may enter Control+C at anytime to bring up the main menu.\n\n")
                    print("You have chosen to start communication as Bob.\n")
                    sharedPrime = eval(input("Please enter the agreed upon prime number: "))
                    Pcheck = isPrime(sharedPrime)
                    if(Pcheck == True):
                        phi = sharedPrime - 1
                        print("\nBased on ", sharedPrime, ", Phi is ", phi)
                    else:
                        print("\n"*50)
                        print(sharedPrime, " is not a prime number, please try again.\n")
                        raise
                    BobKey = eval(input("\nPlease enter Bob's Private key: \t"))
                    primecheck = gcd(BobKey, phi)
                    if(primecheck == 0):
                        print("\n"*50)
                        print("Bob's private key is not relatively prime to phi, please choose again.\n")
                        raise
                    else:
                        Bmodphi = invmod(BobKey, phi)
                        print("\nBob computes ", BobKey, "^-1 mod",phi)
                        print("\nThe inverse mod of the private key is ", Bmodphi)
                    AliceKey = eval(input("\nPlease enter Alice's Private Key: \t"))
                    primecheck = gcd(AliceKey, phi)
                    if(primecheck == 0):
                        print("\n"*50)
                        print("Alice's private key is not relatively prime to phi, please choose again.\n")
                        raise
                    else:
                        Amodphi = invmod(AliceKey, phi)
                        print("\nAlice computes ", AliceKey, "^-1 mod",phi)
                        print("\nThe inverse mod of the private key is ", Amodphi)   
                    k = eval(input("\nEnter your Secret Key(k) Value: \t"))
                    if k >= phi:
                        print("\nYour Secret Key must be less than the Shared Prime minus 1.")
                        print("\nPlease try again.")
                        raise
                    k1 = (k**BobKey % sharedPrime)
                    print("\n\nBob computes ", k,"^",BobKey,"mod",sharedPrime, "=", k1)
                    print("\nBob sends ", k1, " to Alice ---------------->\n")
                    k2 = (k1**AliceKey % sharedPrime)
                    print("\n\t\t\tAlice computes ", k1,"^",AliceKey,"mod", sharedPrime, "=", k2)
                    print("\n\t             <---------------- Alice sends ", k2, " to Bob\n")
                    k3 = (k2**Bmodphi % sharedPrime)
                    print("\nBob computes ", k2,"^",Bmodphi,"mod", sharedPrime, "=", k3)
                    print("\nBob sends ", k3, " to Alice ---------------->\n")
                    k4 = (k3**Amodphi % sharedPrime)
                    print("\n\t\t\tAlice computes ", k3,"^",Amodphi,"mod", sharedPrime, "=", k4)
                    print("\n\t\t\tAlice now has the shared secret key!", k4,"\n")
        except(ValueError, NameError, SyntaxError, RuntimeError):
                print("\nBad input, try again.\n")
        except KeyboardInterrupt:
                    main()
                
    print("\nThank you")
    print("\n\t\tfor using")
    print("\nmy program!")
    print("\n\t\tGood Bye!")
main()

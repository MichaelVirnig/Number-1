# Michael Virnig
# RSA Encryption/Decryption

def getText(t): #validates the text, and raises and error if not valid chars
    LV = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while True:
        try:
            text = t.lower()#make the string all lowercase
            raw = text.replace(" ","")#remove spaces
            text1 = []
            for char in raw:
                if char in LV:
                    text1.append(char)
                if char not in LV:
                    raise
            text1 = ''.join(text1)
            return text1
        except:
            print("\nERROR: Please do not use special characters or numbers with text.\n")
            menu == MENU()

def invmod(p, q): #Inv Mod function
    m = q; d0 = q; d1 = p; x0 = 0; x1 = 1
    while d1 != 0:
        q = int(d0/d1)
        d2 = (d0-(q*d1))
        x2 = (x0-(q*x1))
        x0 = x1; x1 = x2; d0 = d1; d1 = d2
    mod1 = int(x0%m)
    return mod1

def gcd(a, b): #for relatively prime check
    n = a; m = b
    while n != 0:
        n, m = m%n, n
    if m == 1:
        return 1
    else:
        return 0

def isPrime(n): #validates if the number is prime
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

def modexp(y,x,n):#base, exp, mod
    a = x
    c = y
    b = 1
    while a != 0:
        if(a%2 == 0):
            c =(c*c)%n
            a=(a/2)
        else:
            b=(b*c)%n
            a=(a-1)
    return b

def textencrypt(x, y, z): # m value, encrypt key, n (encrypts and decrypts)
    C = []
    new = len(x)
    count = 0
    try:
        while count != new:
            temp = modexp(x[count],y,z)
            C.append(temp)
            count += 1
        return C
    except NameError:
        print("\nERROR: Something went wrong with the encryption, try again.\n")
        raise KeyboardInterrupt

def intencrypt(x, y, z): # m value, encrypt key, n (encrypts and decrypts)
    try:
        temp = modexp(x,y,z)
        return temp
    except:
        print("\nERROR: Something went wrong with the encryption, try again.\n")
        raise KeyboardInterrupt

def intconv(u): #returns index value of text in 26 chat codelist
    listA = []
    text = u.lower()
    rawtext = text.replace(" ","")
    codelist = "abcdefghijklmnopqrstuvwxyz"
    for i in rawtext:
        x = codelist.index(i)
        listA.append(x)
    return listA

def charconv(v):
    listB = []
    codelist = "abcdefghijklmnopqrstuvwxyz"
    for i in v:
        x = codelist[i]
        listB.append(x)
    return listB
            
def MENU():
    while True:
        try:
            menu = eval(input("\nPlease select from the following choices:\n"
                         "\n\t1) Bob and Kathy\n"
                         "\n\t2) Bob and Flynn\n"
                         "\n\t3) Kathy and Flynn\n"
                         "\n\t4) Exit the program\n"
                         "\nEnter your choice (1 || 2 || 3 || 4): "))
            if (1 <= menu <= 4):
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
    while menu != 4:
        menu = MENU() # call the menu
        try:
                if menu != 4: #Bob, Kathy, and Flynn
                    print("\nWelcome to my RSA program!\n")
                    print("You may enter Control+C at anytime to bring up the main menu.\n\n")
                    print("First lets fill out Bob, Kathy and Flynns key info.")
                    print("\nHere are some small primes to help get you started.")
                    print("\n3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97\n")
                    Pb = eval(input("Please enter Bob's P: "))
                    Pbcheck = isPrime(Pb) # prime check P
                    if(Pbcheck == True):
                        Pbphi = Pb - 1
                    else:
                        print("\n"*50)
                        print(Pb, " is not a prime number, please try again.\n")
                        raise
                    Qb = eval(input("\nPlease enter Bob's Q: "))
                    Pbcheck = isPrime(Qb) # prime check Q
                    if(Pbcheck == True):
                        Qbphi = Qb - 1
                        Bphi = Pbphi*Qbphi # get phi(n)
                        Nb = Pb*Qb # get N
                    else:
                        print("\n"*50)
                        print(Qb, " is not a prime number, please try again.\n")
                        raise
                    Eb = eval(input("\nEnter Bob's E: "))
                    PrimeCheck = gcd(Eb,Bphi) # prime check E
                    if PrimeCheck == 1 and Eb < Bphi:
                        pass
                    elif PrimeCheck == 0:
                        print()
                        print(Eb,"is not relatively prime to",Bphi,"lets start over.\n")
                        raise
                    elif Eb > Bphi:
                        print()
                        print("The encryption key cannot be larger than",Bphi,"lets start over.\n")
                        raise
                    Db = invmod(Eb,Bphi) #Bobs private key
                    print("\nP =", Pb,", Q =",Qb, ", N =",Nb,", E =",Eb,", D =",Db,", and Phi =", Bphi)
                    print("\n"*50)
                    print("\n3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97")
                    Pk = eval(input("\n\nPlease enter Kathy's P: "))
                    Pkcheck = isPrime(Pk) # prime check P
                    if(Pkcheck == True):
                        Pkphi = Pk - 1
                    else:
                        print("\n"*50)
                        print(Pk, " is not a prime number, please try again.\n")
                        raise
                    Qk = eval(input("\nPlease enter Kathy's Q: "))
                    Pkcheck = isPrime(Qk) # prime check Q
                    if(Pkcheck == True):
                        Qkphi = Qk - 1
                        Kphi = Pkphi*Qkphi # get phi(n)
                        Nk = Pk*Qk # get N
                    else:
                        print("\n"*50)
                        print(Q, " is not a prime number, please try again.\n")
                        raise
                    Ek = eval(input("\nPlease enter Kathy's E: "))
                    PrimeCheck = gcd(Ek,Kphi) # prime check E
                    if PrimeCheck == 1 and Ek < Kphi:
                        pass
                    elif PrimeCheck == 0:
                        print()
                        print(Ek,"is not relatively prime to Phi:",Kphi,"lets start over.\n")
                        raise
                    elif Ek > Kphi:
                        print()
                        print("The encryption key cannot be larger than Phi:",Kphi,"lets start over.\n")
                        raise
                    Dk = invmod(Ek,Kphi) # Kathys private key
                    print("\nP = ", Pk,", Q =",Qk, ", N =",Nk,", E =",Ek,", D =",Dk,", and Phi is ", Kphi)
                    print("\n"*50)
                    print("\n3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97")
                    Pf = eval(input("\n\nPlease enter Flynn's P: "))
                    Pfcheck = isPrime(Pf) # prime check P
                    if(Pfcheck == True):
                        Pfphi = Pf - 1
                    else:
                        print("\n"*50)
                        print(Pf, " is not a prime number, please try again.\n")
                        raise
                    Qf = eval(input("\nPlease enter Flynn's Q: "))
                    Pfcheck = isPrime(Qf) # prime check Q
                    if(Pfcheck == True):
                        Qfphi = Qf - 1
                        Fphi = Pfphi*Qfphi # get phi(n)
                        Nf = Pf*Qf # get N
                    else:
                        print("\n"*50)
                        print(Qf, " is not a prime number, please try again.\n")
                        raise
                    Ef = eval(input("\nPlease enter Flynn's E: "))
                    PrimeCheck = gcd(Ef,Fphi)
                    if PrimeCheck == 1 and Ef < Fphi:
                        pass
                    elif PrimeCheck == 0:
                        print()
                        print(Ef,"is not relatively prime to Phi:",Fphi,"try again.\n")
                        raise
                    elif Ef > Fphi:
                        print()
                        print("The encryption key cannot be larger than Phi:",Fphi,"try again.\n")
                        raise
                    Df = invmod(Ef,Fphi)
                    print("\nP =", Pf,", Q =",Qf, ", N=",Nf,", E =",Ef,", D =",Df,", and Phi =", Fphi)
                    print("\n"*50)
                    print("\nBob's public key is: ",Eb,",",Nb) 
                    print("\nBob's private key is: ",Db,",",Nb)
                    print("\nKathy's public key is: ",Ek,",",Nk)
                    print("\nKathy's private key is: ",Dk,",",Nk)
                    print("\nFlynn's public key is: ",Ef,",",Nf)
                    print("\nFlynn's private key is: ",Df,",",Nf)
                    
                    if menu == 1: #Bob and Kathy
                        choice = input("\n\nWould you like to encrypt\n\t(T)ext or (I)nteger\n\t(T || I )? ")
                        if (choice == 'T' or choice == 't'):
                            print("\nBob gets Kathys public key",Ek,",",Nk)
                            text = input("\nNow enter the M value to encrypt: ")
                            M = getText(text)
                            temp = intconv(M)
                            Cm = textencrypt(temp,Ek,Nk) # mod exponentiation using Kathys public key
                            print("\nBob calculates:",temp,"^",Ek,"mod",Nk,"=",Cm)
                            print("\nBob sends Kathy: ",Cm)
                            Dm = textencrypt(Cm,Dk,Nk) # decrypt with mod exp using Kathys private key
                            Dt = charconv(Dm)
                            print("\nKathy receives",Cm)
                            print("\nKathy calculates:",Cm,"^",Dk,"mod",Nk,"=",Dm)
                            print("\nKathy decrypts it to: ",Dm,Dt)
                        if (choice == 'I' or choice == 'i'):
                            print("\nBob gets Kathys public key",Ek,",",Nk)
                            M = eval(input("\nNow enter the M value to encrypt: "))
                            if M >= Nk:
                                print("\nThe message value must be less than",Nk)
                                raise
                            else:
                                Cm = intencrypt(M,Ek,Nk) # mod exponentiation using Kathys public key
                                print("\nBob calculates:",M,"^",Ek,"mod",Nk,"=",Cm)
                                print("\nBob sends Kathy: ",Cm)
                                Dm = intencrypt(Cm,Dk,Nk) # decrypt with mod exp using Kathys private key
                                print("\nKathy receives",Cm)
                                print("\nKathy calculates:",Cm,"^",Dk,"mod",Nk,"=",Dm)
                                print("\nKathy decrypts it to: ",Dm)
                        if (choice not in "T,t,I,i"):
                            print("/nNot a valid choice, T or I, try again.\n")
                            raise KeyboardInterrupt
                        
                    if menu == 2: #Bob and Flynn
                        choice = input("\n\nWould you like to encrypt\n\t(T)ext or (I)nteger\n\t(T || I )? ")
                        if (choice == 'T' or choice == 't'):
                            print("\nBob gets Flynns public key",Ef,",",Nf)
                            text = input("\nNow enter the M value to encrypt: ")
                            M = getText(text)
                            temp = intconv(M)
                            Cm = textencrypt(temp,Ef,Nf) # mod exponentiation using Flynns public key
                            print("\nBob calculates:",temp,"^",Ef,"mod",Nf,"=",Cm)
                            print("\nBob sends Flynn: ",Cm,"----->")
                            Dm = textencrypt(Cm,Df,Nf) # decrypt using Flynns Private key
                            Dt = charconv(Dm)
                            print("\nFlynn receives",Cm)
                            print("\nFlynn calculates:",Cm,"^",Df,"mod",Nf,"=",Dm)
                            print("\nFlynn decrypts it to: ",Dm, Dt)
                        if (choice == 'I' or choice == 'i'):
                            print("\nBob gets Flynns public key",Ek,",",Nk)
                            M = eval(input("\nNow enter the M value to encrypt: "))
                            if M >= Nk:
                                print("\nThe message value must be less than",Nk)
                                raise
                            else:
                                Cm = intencrypt(M,Ef,Nf) # mod exponentiation using Flynns public key
                                print("\nBob calculates:",M,"^",Ef,"mod",Nf,"=",Cm)
                                print("\nBob sends Flynn: ",Cm, "----->")
                                Dm = intencrypt(Cm,Df,Nf) # decrypt using Flynns Private key
                                print("\nFlynn receives",Cm)
                                print("\nFlynn calculates:",Cm,"^",Df,"mod",Nf,"=",Dm)
                                print("\nFlynn decrypts it to: ",Dm)
                        if (choice not in "T,t,I,i"):
                            print("Not a valid choice, T or I, try again.\n")
                            raise KeyboardInterrupt
                        
                    if menu == 3: #Kathy and Flynn
                        choice = input("\n\nWould you like to encrypt\n\t(T)ext or (I)nteger\n\t(T || I )? ")
                        if (choice == 'T' or choice == 't'):
                            print("\nKathy gets Flynns public key",Ef,",",Nf)
                            text = input("\nNow enter the M value to encrypt: ")
                            M = getText(text)
                            temp = intconv(M)
                            Cm = textencrypt(temp,Ef,Nf) # mod exponentiation using Flynns public key
                            print("\nKathy calculates:",temp,"^",Ef,"mod",Nf,"=",Cm)
                            print("\nKathy sends Flynn: ",Cm,"----->")
                            Dm = textencrypt(Cm,Df,Nf) # decrypt using Flynns Private ke
                            Dt = charconv(Dm)
                            print("\nFlynn receives",Cm)
                            print("\nFlynn calculates:",Cm,"^",Df,"mod",Nf,"=",Dm)
                            print("\nFlynn decrypts it to: ",Dm, Dt)
                        if (choice == 'I' or choice == 'i'):
                            M = eval(input("\nNow enter the M value to encrypt: "))
                            if M >= Nk:
                                print("\nThe message value must be less than",Nk)
                                raise
                            else:
                                Cm = intencrypt(M,Ef,Nf) # mod exponentiation using Flynns public key
                                print("\nKathy calculates:",M,"^",Ef,"mod",Nf,"=",Cm)
                                print("\nKathy sends Flynn: ",Cm, "----->")
                                Dm = intencrypt(Cm,Df,Nf) # decrypt using Flynns Private key
                                print("\nFlynn receives",Cm)
                                print("\nFlynn calculates:",Cm,"^",Df,"mod",Nf,"=",Dm)
                                print("\nFlynn decrypts it to: ",Dm)
                        if (choice not in "T,t,I,i"):
                            print("Not a valid choice, T or I, try again.\n")
                            raise KeyboardInterrupt
                        
        except KeyboardInterrupt:
                main()
        except:
                print("\nBad input, try again.\n")
                
    print("\nThank you")
    print("\nfor using")
    print("\nmy program!")
    print("\nGood Bye!")
main()

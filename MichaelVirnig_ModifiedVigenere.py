# Michael Virnig
# Modified Vigenere Cipher

def charconv(j):
    list1 = []
    codelist = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = [q.lower() for q in j]
    try:
        for i in text:
            x = codelist.index(i)
            list1.append(x)
        return list1
    except:
        print("\n"*60)
        print("\nThat is not a valid input, try again\n")
        menu == MENU()

def intconv(u): #converts int to char from codelist
    listA = []
    codelist = "abcdefghijklmnopqrstuvwxyz0123456789"
    for i in u:
        x = codelist[i]
        listA.append(x)
    return listA

def affineEncrypt(pt, k, a):
    #CT = (ax + kx*ptx)%36
    ax = int(a); kx = k; ptx = pt; CT = []; i = 0; count = 0
    while count < len(ptx):
        try:
            kxgcd = gcd(kx[i])
        except:
            print("\n"*60)
            print("\nThe key is not relatively prime to 36, try another key.")
            raise
        temp = ((kxgcd*ptx[i]+ax)%36)
        CT.append(temp)
        i += 1
        count += 1
    return CT

def affineDecrypt(c0,k0,a0):
    ad = int(a0); kd = k0; ctd = c0; DC = []; i = 0; count = 0
    while count < len(ctd):
        try:
            kdgcd = gcd(kd[i])
        except:
            print("\n"*60)
            print("\nThe key is not relatively prime to 36, try another key.")
            raise
        temp = invmod(kdgcd)
        tempD = (((ctd[i] - ad)*temp)%36)
        DC.append(tempD)
        i += 1
        count += 1
    return DC

def gcd(a):
    n = a; m = 36
    while n != 0:
        n, m = m%n, n
    if m == 1:
        return a
    else:
        raise

def invmod(p):
    q = 36; d0 = q; d1 = p; x0 = 0; x1 = 1
    while d1 != 0:
        q = int(d0/d1)
        d2 = (d0-(q*d1))
        x2 = (x0-(q*x1))
        x0 = x1; x1 = x2; d0 = d1; d1 = d2
    mod1 = int(x0%36)
    return mod1

def MENU():
    while True:
        try:
            menu = eval(input("Please select from the following choices:\n"
                         "\n\t1) Encrypt\n"
                         "\n\t2) Decrypt\n"
                         "\n\t3) Exit the program\n"
                         "\nEnter your choice (1 || 2 || 3): "))
            if (1 <= menu <= 3):
                print("\n"*60)
                return menu
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
                print("You chose to Encrypt\n")
                key1 = input("\nPlease enter the Keyword without duplicates: ")
                if key1.isalnum():
                    key1 = key1
                else:
                    raise
                a1 = eval(input("\nPlease enter the Alpha value: "))
                pt1 = input("\nPlease input the Plain Text: ")
                if len(key1) > len(pt1):
                    print("\n"*60)
                    print("\nThe keyword cannot be longer than the Plain Text.\n")
                    menu = MENU()
                    continue
                pt2 = pt1.replace(" ","")
                N = len(key1)
                key2 = []
                while len(key2) < len(pt2):
                    i = 0
                    while i != N and len(key2) < len(pt2):
                        key2.append(key1[i])
                        i = i + 1 
                pt3 = charconv(pt2)
                key3 = charconv(key2)
                e1 = affineEncrypt(pt3, key3, a1)
                e3 = intconv(e1)
                e4 = "".join(str(x) for x in e3)
                print("\nThe Keyword: ", key1, "\n\nThe Alpha: ", a1, "\n\nThe Plain Text: ", pt1)
                print("\nEncrypted message: ",e4)
                print("\nEncryped Integer message: ", e1, "\n")
                menu = MENU()
            if menu == 2:
                print("You chose to Decrypt")
                try:
                    key1
                    print("\nPrevious key for your convenience:\n\nCOPY AND PASTE:  ",key1, "\n")
                except NameError:
                    pass
                key1 = input("Please enter the Keyword without duplicates: ")
                if key1.isalnum():
                    key1 = key1
                else:
                    raise
                try:
                    a1
                    print("\nPrevious Alpha for your convenience:\n\nCOPY AND PASTE:  ",a1, "\n")
                except NameError:
                    pass
                a1 = eval(input("Please enter the Alpha value: "))
                key5 = key1
                a5 = a1
                try:
                    e4
                    print("\nPrevious encrypted text for your convenience:\n\nCOPY AND PASTE:  ",e4, "\n")
                except NameError:
                    pass   
                ct5 = input("Please input the Cipher Text: ")
                ct6 = ct5.replace(" ","")
                N = len(key5)
                key6 = []
                while len(key6) < len(ct6):
                    i = 0
                    while i != N and len(key5) < len(ct6):
                        key6.append(key5[i])
                        i = i + 1 
                ct7 = charconv(ct6)
                key7 = charconv(key6)
                e5 = affineDecrypt(ct7, key7, a5)
                e7 = intconv(e5)
                e8 = "".join(str(x) for x in e7)
                print("\nThe Keyword: ", key5, "\n\nThe Alpha: ", a5, "\n\nThe Cipher Text:   ", ct5)
                print("\nDecrypted message: ",e8)
                print("\nDecryped Integer message: ", e5, "\n")
        except:
            print("\nBad input, try again!\n")
            
    print("Thank you for using my program, Good Bye!")

main()

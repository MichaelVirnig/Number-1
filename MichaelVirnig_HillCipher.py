# Michael Virnig
# Hill Cipher

import string

def getText(t, n): #validates the text, returns integer form
    LV = "abcdefghijklmnopqrstuvwxyz0123456789"
    while True:
        try:
            text1 = ''.join(t)
            text2 = []
            for char in text1:
                if char not in LV:
                    raise
                else:
                    x = LV.index(char)
                    text2.append(x)
            return text2
        except:
            print("\n"*60)
            print("\nERROR: Please check your Text input.\n")
            menu == MENU()

def charList(k): #place input into a list
    char = k
    char1 = []
    for i in char:
        char1.append(i)
    return char1
    
def getKey(k, n): #convert key to integer representation
    LV = "abcdefghijklmnopqrstuvwxyz0123456789"
    while True:
        try:
            key2 = ''.join(k)
            key3 = []
            for i in key2:
                if i not in LV:
                    raise
                else:
                    x = LV.index(i)
                    key3.append(x)
            if(len(key3) > (n*n)):
                raise
            else:
                return key3
        except:
            print("\n"*60)
            print("\nThe Key is too long!!")
            print("\nPlease check your Key input.\n")
            menu == MENU()
            
def Pmessage(PT, n):#adds a z to string of odd length
    PT2 = PT.replace(" ","")
    PT3 = []
    j = 0
    try:
        while(len(PT2) > 0):
            if(n == 2):
                digraph = PT2[:2]
                if(len(PT2) == 1):
                    digraph = "%c%c" % (digraph[0], "z")
                    PT3.append(digraph)
                    PT2 = PT2[1:]
                else:
                    PT3.append(digraph)
                    PT2 = PT2[2:]
            if(n == 3):
                trigraph = PT2[:3]
                if(len(PT2) == 1):
                    trigraph = "%c%c%c" % (trigraph[0], "z", "z")
                    PT3.append(trigraph)
                    PT2 = PT2[1:]
                elif(len(PT2) == 2):
                    trigraph = "%c%c%c" % (trigraph[0], trigraph[1], "z")
                    PT3.append(trigraph)
                    PT2 = PT2[2:]
                else:
                    PT3.append(trigraph)
                    PT2 = PT2[3:]
        return PT3
    except:
        print("\n"*60)
        print("\nERROR: Something went wrong while parsing the message.\n")
        menu == MENU()

def makeMatrix(t2, n, k): # generate n x n matrix
    matrix = []
    count = 0
    try:
        for i in range(k):
            new = []
            for j in range(n):
                new.append(t2[count])
                count += 1
            matrix.append(new)
        return matrix
    except:
        print("\n"*60)
        print("\nERROR: Something went wrong while making the matrix for: ",t2,"\n")
        menu == MENU()

def textMatrix(t7, n, k): # generate k x n matrix
    matrix = []
    count = 0
    t7 = ''.join(t7)
    try:
        for i in range(k):
            new = []
            for j in range(n):
                new.append(t7[count])
                count += 1
            matrix.append(new)
        return matrix
    except:
        print("\n"*60)
        print("\nERROR: Something went wrong while making the matrix for: ",t7,"\n")
        menu == MENU()

def intMatrix(t8, n, k): # generate k x n matrix
    matrix = []
    count = 0
    try:
        for i in range(k):
            new = []
            for j in range(n):
                new.append(t8[count])
                count += 1
            matrix.append(new)
        return matrix
    except:
        print("\n"*60)
        print("\nERROR: Something went wrong while making the matrix for: ",t8,"\n")
        menu == MENU()

def Display(matrix1, matrix2, n): #display the matrix
    try:
        if(n == 2):
            for counter in range(n):
                print("|  ", format(matrix1[counter][0], "^7"), format(matrix1[counter][1], "^7"),"|",
                      format(matrix2[counter][0], "^7"), format(matrix2[counter][1], "^7"),"|")
            print("+++++++++++++++++++++++++++++++")
        if(n == 3):
            for counter in range(n):
                print("|  ", format(matrix1[counter][0], "^7"), format(matrix1[counter][1], "^7"), format(matrix1[counter][2], "^7"), "|",
                      format(matrix2[counter][0], "^7"), format(matrix2[counter][1], "^7"), format(matrix2[counter][2], "^7"), "|")
            print("+++++++++++++++++++++++++++++++")
    except:
        print("\n"*60)
        print("\nERROR: Something went wrong while trying to display the matrices: \n",matrix1, matrix2,"\n")
        menu == MENU()

def DisplayText(matrix1, matrix2, n, k): #display the text matrix
    try:
        if(n == 2):
            for counter in range(k):
                print("|  ", format(matrix1[counter][0], "^7"), format(matrix1[counter][1], "^7"),"|",
                      format(matrix2[counter][0], "^7"), format(matrix2[counter][1], "^7")," |")
            print("+++++++++++++++++++++++++++++++")
        if(n == 3):
            for counter in range(k):
               print("|  ", format(matrix1[counter][0], "^7"), format(matrix1[counter][1], "^7"), format(matrix1[counter][2], "^7"), "|",
                      format(matrix2[counter][0], "^7"), format(matrix2[counter][1], "^7"), format(matrix2[counter][2], "^7"), "|")
            print("+++++++++++++++++++++++++++++++")
    except:
        print("\n"*60)
        print("\nERROR: Something went wrong while trying to display the matrices:\n",matrix1, matrix2,"\n")
        menu == MENU()

def charconv(u):
    listA = []
    codelist = "abcdefghijklmnopqrstuvwxyz0123456789"
    for i in u:
        x = codelist[i]
        listA.append(x)
    return listA

def encrypt(a, b, n):
    C = [0]*len(a)
    if(len(a) == 2 and n == 2):
        C[0] = (a[0]*b[0])+(a[1]*b[2]); C[1] = (a[0]*b[1])+(a[1]*b[3])
    if(len(a) == 4 and n == 2):
        C[0] = (a[0]*b[0])+(a[1]*b[2]); C[1] = (a[0]*b[1])+(a[1]*b[3])
        C[2] = (a[2]*b[0])+(a[3]*b[2]); C[3] = (a[2]*b[1])+(a[3]*b[3])
    if(len(a) == 3 and n == 3):
        C[0] = (a[0]*b[0])+(a[1]*b[3])+(a[2]*b[6]); C[1] = (a[0]*b[1])+(a[1]*b[4])+(a[2]*b[7]); C[2] = (a[0]*b[2])+(a[1]*b[5])+(a[2]*b[8])
    if(len(a) == 6 and n == 3):
        C[0] = (a[0]*b[0])+(a[1]*b[3])+(a[2]*b[6]); C[1] = (a[0]*b[1])+(a[1]*b[4])+(a[2]*b[7]); C[2] = (a[0]*b[2])+(a[1]*b[5])+(a[2]*b[8])
        C[3] = (a[3]*b[0])+(a[4]*b[3])+(a[5]*b[6]); C[4] = (a[3]*b[1])+(a[4]*b[4])+(a[5]*b[7]); C[5] = (a[3]*b[2])+(a[4]*b[5])+(a[5]*b[8])
    if(len(a) == 9 and n == 3):
        C[0] = (a[0]*b[0])+(a[1]*b[3])+(a[2]*b[6]); C[1] = (a[0]*b[1])+(a[1]*b[4])+(a[2]*b[7]); C[2] = (a[0]*b[2])+(a[1]*b[5])+(a[2]*b[8])
        C[3] = (a[3]*b[0])+(a[4]*b[3])+(a[5]*b[6]); C[4] = (a[3]*b[1])+(a[4]*b[4])+(a[5]*b[7]); C[5] = (a[3]*b[2])+(a[4]*b[5])+(a[5]*b[8])
        C[6] = (a[6]*b[0])+(a[7]*b[3])+(a[8]*b[6]); C[7] = (a[6]*b[1])+(a[7]*b[4])+(a[8]*b[7]); C[8] = (a[6]*b[2])+(a[7]*b[5])+(a[8]*b[8])
    ctext = [0]*len(a)
    z = 0
    while(z < len(C)):
        ctext[z] = C[z]%36
        z += 1
    return ctext

def decrypt(a, b, dn):
    D = [0]*len(a)
    if(len(a) == 2 and dn == 2):
        D[0] = (a[0]*b[0])+(a[1]*b[2]); D[1] = (a[0]*b[1])+(a[1]*b[3])
    if(len(a) == 4 and dn == 2):
        D[0] = (a[0]*b[0])+(a[1]*b[2]); D[1] = (a[0]*b[1])+(a[1]*b[3])
        D[2] = (a[2]*b[0])+(a[3]*b[2]); D[3] = (a[2]*b[1])+(a[3]*b[3])
    if(len(a) == 3 and dn == 3):
        D[0] = (a[0]*b[0])+(a[1]*b[3])+(a[2]*b[6]); D[1] = (a[0]*b[1])+(a[1]*b[4])+(a[2]*b[7]); D[2] = (a[0]*b[2])+(a[1]*b[5])+(a[2]*b[8])
    if(len(a) == 6 and dn == 3):
        D[0] = (a[0]*b[0])+(a[1]*b[3])+(a[2]*b[6]); D[1] = (a[0]*b[1])+(a[1]*b[4])+(a[2]*b[7]); D[2] = (a[0]*b[2])+(a[1]*b[5])+(a[2]*b[8])
        D[3] = (a[3]*b[0])+(a[4]*b[3])+(a[5]*b[6]); D[4] = (a[3]*b[1])+(a[4]*b[4])+(a[5]*b[7]); D[5] = (a[3]*b[2])+(a[4]*b[5])+(a[5]*b[8])
    if(len(a) == 9 and dn == 3):
        D[0] = (a[0]*b[0])+(a[1]*b[3])+(a[2]*b[6]); D[1] = (a[0]*b[1])+(a[1]*b[4])+(a[2]*b[7]); D[2] = (a[0]*b[2])+(a[1]*b[5])+(a[2]*b[8])
        D[3] = (a[3]*b[0])+(a[4]*b[3])+(a[5]*b[6]); D[4] = (a[3]*b[1])+(a[4]*b[4])+(a[5]*b[7]); D[5] = (a[3]*b[2])+(a[4]*b[5])+(a[5]*b[8])
        D[6] = (a[6]*b[0])+(a[7]*b[3])+(a[8]*b[6]); D[7] = (a[6]*b[1])+(a[7]*b[4])+(a[8]*b[7]); D[8] = (a[6]*b[2])+(a[7]*b[5])+(a[8]*b[8])
    z = 0
    dtext = [0]*len(a)
    while(z < len(D)):
        dtext[z] = D[z]%36
        z += 1
    return dtext

def determinant(A, n):
    try:
        if(n == 2):
            det = (A[0]*A[3])-(A[1]*A[2])
            det1 = (det%36)
            det2 = gcd(det1)
            if det2 == 1:
                return det1
            else:
                return 0
        if(n == 3):
            det = ((A[0]*(A[4]*A[8]-A[5]*A[7]))-((A[1]*(A[3]*A[8]-A[5]*A[6])))+((A[2]*(A[3]*A[7]-A[4]*A[6]))))
            det1 = (det%36)
            det2 = gcd(det1)
            if det2 == 1:
                return det1
            else:
                return 0
    except:
        print("\n"*60)
        print("\nERROR: Something went wrong while calculating the determinant.\n")
        menu == MENU()

def adjoint(A, n):#create adjoint matrix
    adjlist = []
    try:
        if(n == 2):
            M11 = A[0]%36
            M12 = ((-1)*(A[2]))%36
            M21 = ((-1)*(A[1]))%36
            M22 = A[3]%36
            adjlist.append(M22)
            adjlist.append(M21)
            adjlist.append(M12)
            adjlist.append(M11)
            return adjlist
        elif(n == 3):
            M11 = (A[4]*A[8]-A[7]*A[5])%36
            M12 = ((A[3]*A[8]-A[6]*A[5])*-1)%36
            M13 = (A[3]*A[7]-A[6]*A[4])%36
            M21 = ((A[1]*A[8]-A[7]*A[2])*-1)%36
            M22 = (A[0]*A[8]-A[6]*A[2])%36
            M23 = ((A[0]*A[7]-A[6]*A[1])*-1)%36
            M31 = (A[1]*A[5]-A[4]*A[2])%36
            M32 = ((A[0]*A[5]-A[3]*A[2])*-1)%36
            M33 = (A[0]*A[4]-A[3]*A[1])%36
            adjlist.append(M11)
            adjlist.append(M21)
            adjlist.append(M31)
            adjlist.append(M12)
            adjlist.append(M22)
            adjlist.append(M32)
            adjlist.append(M13)
            adjlist.append(M23)
            adjlist.append(M33)
            return adjlist
    except:
        print("\n"*60)
        print("\nERROR: Something went wrong while creating the adjoint matrix.\n")

def inverse(C, D): #adj/det(k)
    #C = adjlist, D = determinant
    D1 = invmod(D)
    kinv2 = []
    for j in C:#muliply by the determinant inverse then mod 36 each term
        y = (D1*j)%36
        kinv2.append(y)
    return kinv2
        
def invmod(p):
    q = 36; d0 = q; d1 = p; x0 = 0; x1 = 1
    while d1 != 0:
        q = int(d0/d1)
        d2 = (d0-(q*d1))
        x2 = (x0-(q*x1))
        x0 = x1; x1 = x2; d0 = d1; d1 = d2
    mod1 = int(x0%36)
    return mod1

def gcd(a):
    n = a; m = 36
    while n != 0:
        n, m = m%n, n
    if m == 1:
        return 1
    else:
        return 0


def MENU():
    while True:
        try:
            menu = eval(input("Please select from the following choices:"
                         "\n\t1) Encrypt"
                         "\n\t2) Decrypt"
                         "\n\t3) Exit the program"
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
                print("You have chosen to Encrypt\n")
                n = eval(input("Select Key Matrix Size\n2 for 2x2:\n3 for 3x3:   "))
                if(n != 2 and n != 3):
                    print("\n"*60)
                    print("Only enter 2 or 3.")
                    raise
                k1 = input("Please enter the key: ").lower()
                k1 = k1.replace(" ","")
                if(len(k1) <  n*n):
                    print("\nThe key must be ",n,"x",n,"\n")
                    raise
                k2 = getKey(k1, n)#get integer list
                k3 = charList(k1)#place key into a list
                t1 = input("Please enter the text: ").lower()
                t1 = t1.replace(" ","")
                if(len(t1) <  n):
                    raise
                pt1 = Pmessage(t1, n)#pad with z and produce di/trigraphs
                pt2 = getText(pt1, n)#get integers list
                if(len(pt2) == 2 and n == 2):
                    k = 1
                    ct = encrypt(pt2, k2, n)
                    ct1 = charconv(ct)
                    m1 = makeMatrix(k2, n, n)
                    m2 = makeMatrix(k3, n, n)
                    m3 = textMatrix(pt1, n, k)
                    m4 = makeMatrix(pt2, n, k)
                    m5 = makeMatrix(ct, n, k)
                    m6 = textMatrix(ct1, n, k)
                if(len(pt2) == 4 and n == 2):
                    k = 2
                    ct = encrypt(pt2, k2, n)
                    ct1 = charconv(ct)
                    m1 = makeMatrix(k2, n, n)
                    m2 = makeMatrix(k3, n, n)
                    m3 = textMatrix(pt1, n, k)
                    m4 = makeMatrix(pt2, n, k)
                    m5 = makeMatrix(ct, n, k)
                    m6 = textMatrix(ct1, n, k)
                if(len(pt2) == 6 and n ==3):#set kxn size
                    k = 2
                    ct = encrypt(pt2, k2, n)
                    ct1 = charconv(ct)
                    m1 = makeMatrix(k2, n, n)
                    m2 = makeMatrix(k3, n, n)
                    m3 = textMatrix(pt1, n, k)
                    m4 = makeMatrix(pt2, n, k)
                    m5 = makeMatrix(ct, n, k)
                    m6 = textMatrix(ct1, n, k)
                if(len(pt2) == 9 and n ==3):#set kxn size
                    k = 3
                    ct = encrypt(pt2, k2, n)
                    ct1 = charconv(ct)
                    m1 = makeMatrix(k2, n, n)
                    m2 = makeMatrix(k3, n, n)
                    m3 = textMatrix(pt1, n, k)
                    m4 = makeMatrix(pt2, n, k)
                    m5 = makeMatrix(ct, n, k)
                    m6 = textMatrix(ct1, n, k)
                if(2 <= len(pt2) > 4 and n == 2):
                    k = int(len(pt2)/2)
                    i = 0
                    CT = []
                    CT1 = []
                    pt3 = pt2
                    while(i < len(pt3)):
                        ct = encrypt(pt3[:2], k2, n)
                        CT.append(ct)
                        CT1 += ct
                        pt3 = pt3[2:]
                    ct1 = charconv(CT1)
                    m1 = makeMatrix(k2, n, n)
                    m2 = makeMatrix(k3, n, n)
                    m3 = textMatrix(pt1, n, k)
                    m4 = makeMatrix(pt2, n, k)
                    m5 = makeMatrix(CT1, n, k)
                    m6 = textMatrix(ct1, n, k)
                if(3 <= len(pt2) > 9 and n == 3):
                    k = int(len(pt2)/3)
                    i = 0
                    CT = []
                    CT1 = []
                    pt3 = pt2
                    while(i < len(pt3)):
                        ct = encrypt(pt3[:3], k2, n)
                        CT.append(ct)
                        CT1 += ct
                        pt3 = pt3[3:]
                    ct1 = charconv(CT1)
                    m1 = makeMatrix(k2, n, n)
                    m2 = makeMatrix(k3, n, n)
                    m3 = textMatrix(pt1, n, k)
                    m4 = makeMatrix(pt2, n, k)
                    m5 = makeMatrix(CT1, n, k)
                    m6 = textMatrix(ct1, n, k)
                
                print("++++++++KEY MATRICES+++++++++++")
                Display(m2, m1, n)
                print("++++++++TEXT MATRICES++++++++++")
                DisplayText(m3, m4, n, k)
                print("+++++CIPHERTEXT MATRICES+++++++")
                DisplayText(m6, m5, n, k)
                Det = determinant(k2, n)
                if Det == 0:
                    print("\n"*60)
                    print("Key inverse could not be made because the determinant was not coprime to 36.\n\nPlease choose another key.\n")
                else:
                    Adj = adjoint(k2, n)
                    Kinv = inverse(Adj, Det)
                    m7 = makeMatrix(Kinv, n, n)
                    print("++++++K & K INVERSE MATRIX++++++++")
                    Display(m1, m7, n)
                    ct1 = ''.join(ct1)
                    print("CipherText string (Copy before proceeding): ", ct1, "\n")

            if menu == 2:
                print("You have chosen to Decrypt\n")
                dn = eval(input("Select Key Matrix Size\n2 for 2x2:\n3 for 3x3:   "))
                if(dn != 2 and dn != 3):
                    print("\n"*60)
                    print("Only enter 2 or 3.")
                    raise
                dk1 = input("Please enter the key: ").lower()
                dk1 = dk1.replace(" ","")#strip spaces from string
                if(len(dk1) <  n*n):
                    print("\nThe key must be ",dn,"x",dn,"\n")
                    raise
                dk2 = getKey(dk1, dn)#get integer form for input
                dk3 = charList(dk1) #place input into a list
                d1 = input("Please enter the Cipher text characters: ").lower()
                if(len(d1) < n):
                    raise
                d1 = d1.replace(" ","")#strip spaces from string
                d2 = Pmessage(d1, dn)#place message into digraph/trigraphs
                dt1 = getText(d2, dn)#convert to integer form
                if(len(dt1)%2 > 0 and dn == 2):#raise error if odd length
                    print("\n"*60)
                    print("\nYour cipher text is of odd length,"
                          " please check your code and try again.\n")
                    raise
                Det1 = determinant(dk2, dn)#calculate the determinant of the key
                if Det1 == 0:
                    print("\n"*60)
                    print("The determinant was not coprime to 36, please choose another key.\n")
                else:
                    Adj1 = adjoint(dk2, dn)#get cofactors and adjoint
                    Kinv1 = inverse(Adj1, Det1)#get k inverse
                    m8 = makeMatrix(dk2, dn, dn)
                    m14 = makeMatrix(Kinv1, dn, dn)
                    print("+++++K & K INVERSE MATRIX++++++")
                    Display(m8, m14, dn)
                if(len(dt1) == 2 and dn == 2):#exe if 1x2
                    dk = 1
                    m8 = makeMatrix(dk2, dn, dn)
                    m9 = makeMatrix(dk3, dn, dn)
                    dpt1 = charconv(dt1)
                    dpt = decrypt(dt1, Kinv1, dn)
                    dt3 = charconv(dpt)
                    m10 = intMatrix(dt1, dn, dk)
                    m11 = textMatrix(dt3, dn, dk)
                    m12 = textMatrix(dpt1, dn, dk)
                    m13 = intMatrix(dpt, dn, dk)
                if(len(dt1) == 4 and dn == 2):#exe if 2x2
                    dk = 2
                    m8 = makeMatrix(dk2, dn, dn)
                    m9 = makeMatrix(dk3, dn, dn)
                    dpt1 = charconv(dt1)
                    dpt = decrypt(dt1, Kinv1, dn)
                    dt3 = charconv(dpt)
                    m10 = intMatrix(dt1, dn, dk)
                    m11 = textMatrix(dt3, dn, dk)
                    m12 = textMatrix(dpt1, dn, dk)
                    m13 = intMatrix(dpt, dn, dk)
                if(len(dt1) == 6 and dn == 3):#exe if 2x3
                    dk = 2
                    m8 = makeMatrix(dk2, dn, dn)
                    m9 = makeMatrix(dk3, dn, dn)
                    dt3 = charconv(dt1)
                    m10 = intMatrix(dt1, dn, dk)
                    m11 = textMatrix(dt3, dn, dk)
                    dpt = decrypt(dt1, Kinv1, dn)
                    dpt1 = charconv(dpt)
                    m12 = textMatrix(dpt1, dn, dk)
                    m13 = intMatrix(dpt, dn, dk)
                if(len(dt1) == 9 and dn == 3):#exe if 3x3
                    dk = 3
                    m8 = makeMatrix(dk2, dn, dn)
                    m9 = makeMatrix(dk3, dn, dn)
                    dt3 = charconv(dt1)
                    m10 = intMatrix(dt1, dn, dk)
                    m11 = textMatrix(dt3, dn, dk)
                    dpt = decrypt(dt1, Kinv1, dn)
                    dpt1 = charconv(dpt)
                    m12 = textMatrix(dpt1, dn, dk)
                    m13 = intMatrix(dpt, dn, dk)
                if(len(dt1) > 4 and dn == 2):#exe if larger then 2x2
                    dk = int(len(dt1)/2)
                    i = 0
                    DT = []
                    DT1 = []
                    dt4 = dt1
                    while(i < len(dt4)):
                        dt = decrypt(dt4[:2], Kinv1, dn)
                        DT.append(dt)
                        DT1 += dt
                        dt4 = dt4[2:]
                    m8 = makeMatrix(dk2, dn, dn)
                    m9 = makeMatrix(dk3, dn, dn)
                    dt3 = charconv(DT1)
                    dpt1 = charconv(dt1)
                    m10 = intMatrix(dpt1, dn, dk)
                    m11 = textMatrix(dt3, dn, dk)
                    m12 = intMatrix(dt1, dn, dk)
                    m13 = intMatrix(DT1, dn, dk)
                if(len(dt1) > 9 and dn == 3):#exe if larger then 3x3
                    dk = int(len(dt1)/3)
                    i = 0
                    DT = []
                    DT1 = []
                    dt4 = dt1
                    while(i < len(dt4)):
                        dt = decrypt(dt4[:3], Kinv1, dn)
                        DT.append(dt)
                        DT1 += dt
                        dt4 = dt4[3:]
                    m8 = makeMatrix(dk2, dn, dn)
                    m9 = makeMatrix(dk3, dn, dn)
                    dt3 = charconv(DT1)
                    dpt1 = charconv(dt1)
                    m10 = intMatrix(dpt1, dn, dk)
                    m11 = textMatrix(dt3, dn, dk)
                    m12 = intMatrix(dt1, dn, dk)
                    m13 = intMatrix(DT1, dn, dk)
                print("+++++++++KEY MATRICES++++++++++")
                Display(m9, m8, dn)
                print("+++++CIPHER TEXT MATRICES++++++")
                DisplayText(m10, m12, dn, dk)
                print("+++++PLAIN TEXT MATRICES+++++++")
                DisplayText(m11, m13, dn, dk)
                dt3 = ''.join(dt3)
                print("The plain text message: ",dt3,"\n")

        except:
            print("\nBad input, try again.\n")

    print("\nThank you")
    print("\n\tfor using")
    print("\n\t\tmy program!")
    print("\n\t\t\tGood Bye!")

main()

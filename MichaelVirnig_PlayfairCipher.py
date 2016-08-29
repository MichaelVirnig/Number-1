# Michael Virnig
# Playfair Cipher
import time

def getKey(k): #creates a full list containing all key chars and LV chars
    LV = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
      'o','p','q','r','s','t','u','v','w','x','y','z','0','1',
      '2','3','4','5','6','7','8','9']
    while True:
        try:
            key = k.lower()#make the string all lowercase
            rawk = key.replace(" ","")#remove spaces
            rawk = ''.join(sorted(set(rawk), key = rawk.index))#remove commas and keep in orignal order
            key1 = []
            for char in rawk:
                if char in LV:
                    key1.append(char)
                if char not in LV:
                    raise
            for char in LV:
                if char not in key1:
                    key1.append(char)
            if len(key1) > 36:
                print("\nThe Key is too long!!")
                break
            return key1
        except:
            print("\nERROR: Please do not use special characters.\n")
            menu == MENU()

def getText(t): #validates the text, and raises and error if not valid chars
    LV = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
      'o','p','q','r','s','t','u','v','w','x','y','z','0','1',
      '2','3','4','5','6','7','8','9']
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
            return text1
        except:
            print("\nERROR: Please do not use special characters.\n")
            menu == MENU()

def pmessage(PT): #parse the message to check for doubles and odd length
        PT1 = ''.join(PT)#combines the list with no commas
        PT2 = []
        j = 0
        if((len(PT1)%2) == '0'):#checks if message length is even
            while(j < len(PT1)):
                if(PT1[j] != PT1[j+1]):
                    PT2.append(PT1[j])
                    PT2.append(PT1[j+1])
                    j+=2
                else:
                    PT2.append(PT1[j])
                    PT2.append("z")#place a z if there is a duplicate pair
                    j+=1
        else:#if length is odd
            while(j < len(PT1)-1):
                if(PT1[j] != PT1[j+1]):
                    PT2.append(PT1[j])
                    PT2.append(PT1[j+1])
                    j+=2
                else:
                    PT2.append(PT1[j])
                    PT2.append("z")#place a z if there is a duplicate pair
                    j+=1
        if(j != len(PT1)):
            PT2.append(PT1[j])#adds the final char that wasnt compared
        if((len(PT2)%2) != 0):#checks if finished list is odd
            PT2.append("z")#place a z if the end length of PT is odd
        return PT2

def makeMatrix(key2):#generate the 6x6 lines for the matrix
    matrix = []
    count = 0
    for i in range(6):
        new = []
        for j in range(6):
            new.append(key2[count])
            count += 1
        matrix.append(new)
    return matrix

def Display(matrix): #display the matrix in 6x6 format
    print("\t     0 1 2 3 4 5")
    print("\t     - - - - - -")
    num = 0
    for counter in range(6):
        print("\t",num,"|",matrix[counter][0], matrix[counter][1], matrix[counter][2],
              matrix[counter][3], matrix[counter][4], matrix[counter][5],"|"); num += 1
    print("\t     - - - - - -")
    print("+++++++++++++++++++++++++++++++++\n")

def getrow(r): #checks character row number for comparison
        if 0<=r<=5:
            row = 1
        elif 6<=r<=11:
            row = 2
        elif 12<=r<=17:
            row = 3
        elif 18<=r<=23:
            row = 4
        elif 24<=r<=29:
            row = 5
        elif 30<=r<=35:
            row = 6
        return row
    
def encrypt(text, key):
        ct = []
        PL2 = text
        e = 0
        while(e < len(PL2)):
            c1 = key.index(PL2[e]) #c1, c2 grab 2 chars to compare
            c2 = key.index(PL2[e+1])
            r1 = getrow(c1)#Check if in the same row
            r2 = getrow(c2)#Check if in the same row
            complist = [5,11,17,23,29]
            if (r1 == r2): #If they are in same row execute rule 1
                if(c1 in complist):
                    c1a = key[(((c1+1)%36)-6)]
                    ct.append(c1a)
                    c2a = key[(c2+1)%36]
                    ct.append(c2a)
                    e += 2
                elif(c2 in complist):
                    c1a = key[(c1+1)%36]
                    ct.append(c1a)
                    c2a = key[(((c2+1)%36)-6)]
                    ct.append(c2a)
                    e += 2
                else:
                    c1a = key[(c1+1)%36]
                    ct.append(c1a)
                    c2a = key[(c2+1)%36]
                    ct.append(c2a)
                    e += 2
            elif (c1%6 == c2%6): #If in same column execute rule 2
                if c1 > 29:
                    c1a = key[(c1+6)%36]
                    ct.append(c1a)
                    c2a = key[c2+6]
                    ct.append(c2a)
                    e += 2
                elif c2 > 29:
                    c1a = key[c1+6]
                    ct.append(c1a)
                    c2a = key[(c2+6)%36]
                    ct.append(c2a)
                    e += 2
                else:
                    c1a = key[c1+6]
                    ct.append(c1a)
                    c2a = key[c2+6]
                    ct.append(c2a)
                    e += 2
            elif (r1 != r2 and c1%6 != c2%6): #If not in same row or column execute rule 3
                col1 = c1%6
                col2 = c2%6
                if col1 > col2:
                    cdif = col1 - col2
                    c1a = key[c1-cdif]
                    ct.append(c1a)
                    c2a = key[c2+cdif]
                    ct.append(c2a)
                    e += 2
                else:
                    cdif = col2 - col1
                    c1a = key[c1+cdif]
                    ct.append(c1a)
                    c2a = key[c2-cdif]
                    ct.append(c2a)
                    e += 2
        return ct
        
def decrypt(text, key):
        dt = []
        PL3 = ''.join(text)
        d = 0
        while(d < len(PL3)):
            d1 = key.index(PL3[d]) #grab 2 chars to compare
            d2 = key.index(PL3[d+1])
            r1 = getrow(d1)#Check if in the same row
            r2 = getrow(d2)#Check if in the same row
            if (r1 == r2): #If they are in same row execute rule 1
                if(d1%6 == 0):#checks for wraparound
                    d1b = key[d1+5]
                    dt.append(d1b)
                    d2b = key[(d2-1)]
                    dt.append(d2b)
                    d += 2
                elif(d2%6 == 0):#checks for wraparound
                    d1b = key[(d1-1)]
                    dt.append(d1b)
                    d2b = key[d2+5]
                    dt.append(d2b)
                    d += 2
                else:
                    d1b = key[(d1-1)]
                    dt.append(d1b)
                    d2b = key[(d2-1)]
                    dt.append(d2b)
                    d += 2
            elif (d1%6 == d2%6):  #If in same column execute rule 2
                if d1 <= 5:
                    d1b = key[(d1+30)]
                    dt.append(d1b)
                    d2b = key[d2-6]
                    dt.append(d2b)
                    d += 2
                elif d2 <= 5:
                    d1b = key[d1-6]
                    dt.append(d1b)
                    d2b = key[(d2+30)]
                    dt.append(d2b)
                    d += 2
                else:
                    d1b = key[d1-6]
                    dt.append(d1b)
                    d2b = key[d2-6]
                    dt.append(d2b)
                    d += 2
            elif (r1 != r2 and d1%6 != d2%6):#If not in same row or column execute rule 3
                col1 = d1%6
                col2 = d2%6
                if col1 < col2:
                    cdif = (col2 - col1)
                    d1b = key[d1+cdif]
                    dt.append(d1b)
                    d2b = key[d2-cdif]
                    dt.append(d2b)
                    d += 2
                if col1 > col2:
                    cdif = (col1 - col2)
                    d1b = key[(d1-cdif)]
                    dt.append(d1b)
                    d2b = key[(d2+cdif)]
                    dt.append(d2b)
                    d += 2
        return dt

def zremove(w):
    i = 0
    zdt = []
    while(i < len(w)-2):#runs through all but the last index value
        w1 = w[i]; w2 = w[i+1]; w3 = w[i+2]
        if(w1 == w3 and w2 == "z"):
            zdt.append(w1)
            i += 2
        else:
            zdt.append(w1)
            zdt.append(w2)
            i += 2
    while(i < len(w)):#checks the last index value 
        if(w[i] != "z"):
            zdt.append(w[i])
            i += 1 #add one to i incase there is an extra character the function missed
        elif(zdt[-1] in 'aeiou' and w[i] == "z" and len(zdt)%2 != 0):
            zdt.append(w[i])
            i += 1
        else:
            i += 1
    return zdt

def MENU():
    while True:
        try:
            menu = int(input("Please select from the following choices:"
                         "\n\t1) Encrypt"
                         "\n\t2) Decrypt"
                         "\n\t3) Exit the program"
                         "\nEnter your choice (1 || 2 || 3): "))
            if (1 <= menu <= 3):
                return menu
                break
            else:
                raise
        except:
            time.sleep(.15)
            print("\nThat is not a valid input, try again.\n"); time.sleep(.5)

def main():
    menu = 0
    while menu != 3:
        menu = MENU()
        try:
            if menu == 1:
                print("You have chosen to Encrypt")
                t1 = input("Please enter the text: ")
                pt1 = getText(t1)
                pt2 = pmessage(pt1)
                pt3 = ''.join(pt2)
                k1 = input("Please enter the key: "); time.sleep(.25)
                k2 = getKey(k1)
                m1 = makeMatrix(k2)
                print("\nYou entered text: ", t1, "\n"); time.sleep(.25)
                print("You entered key:  ", k1, "\n"); time.sleep(.25)
                print("++++++++++++KEY MATRIX+++++++++++")
                Display(m1)
                print("Message to Encrypt is: ", pt3, "\n"); time.sleep(.25)
                ctext = encrypt(pt3, k2)
                ciphertext = ''.join(ctext)
                print("The Encrypted Message: ", ciphertext, "\n"); time.sleep(.25)

            if menu == 2:
                print("You have chosen to Decrypt")
                print("\nHighlight, Copy, and Paste from above if decrypting previous message\n")
                c1 = input("Please enter the Cipher text: ")
                ct1 = getText(c1)
                if(len(ct1)%2 != 0):
                    print("\nYour cipher text is of odd length,"
                          " please check your code and try again.\n"); time.sleep(.5)
                else:
                    ct2 = ''.join(ct1)
                    ck1 = input("Please enter the key: "); time.sleep(.25)
                    ck2 = getKey(ck1)
                    m2 = makeMatrix(ck2)
                    print("\nYou entered the key: ", ck1, "\n"); time.sleep(.25)
                    print("++++++++++++KEY MATRIX+++++++++++")
                    Display(m2)
                    ptext = decrypt(ct1, ck2)
                    pt = ''.join(ptext)
                    print("\nYou entered the text:  ", ct2, "\n"); time.sleep(.25)
                    print("The Decrypted Message: ", pt, "\n"); time.sleep(.25)
                    dtz = zremove(pt)
                    ptz = ''.join(dtz)
                    print("The Orignal Message:   ", ptz, "\n"); time.sleep(.25)
                    
        except NameError:
            time.sleep(.5)
            print("\nThat is not a valid input, try again.\n"); time.sleep(.5)

    print("\n\t\t\tThank you"); time.sleep(.25)
    print("\n\t\tfor using"); time.sleep(.35)
    print("\n\tmy program!"); time.sleep(.45)
    print("\nGood Bye!")

main()

        

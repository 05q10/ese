import numpy as np

def caesar(text,key):
    result=""
    for ch in text.lower():
        if 'a'<=ch<='z':
            result+=chr(((ord(ch)-97+key)%26)+97)
        else:
            result+=ch
    return result

def caesar_decrypt(text,key):
    return caesar(text,26-key)

#MONO
mono_key=list('qwertyuiopasdfghjklzxcvbnm')
def mono(text):
    result=""  
    for ch in text.lower():
        if 'a'<=ch<='z':
            result+=(mono_key[(ord(ch)-97)])
        else:
            result+=ch
    return result

def mono_decrypt(text):
    result="" 
    for ch in text.lower():
        if 'a'<=ch<='z':
            idx=mono_key.index(ch)
            result+=chr(idx+97)
        else:
            result+=ch

    return result

#PLAYFAIR
pf_key=[
    list("playf"),
    list("irbcd"),
    list("eghkm"),
    list("noqst"),
    list("uvwxy")
]

def pf_find(pfkey,a,b):
    pos=[0]*4
    for i in range(5):
        for j in range(5):
            if pfkey[i][j]==a:
                pos[0],pos[1]=i,j
            if pfkey[i][j]==b:
                pos[2],pos[3]=i,j

    return pos

def pf_prepare(text):
    text=text.lower().replace("j","i")
    cleaned=""
    for ch in text:
        if 'a'<=ch<='z':
            cleaned+=ch
    result="" 
    i=0
    while i<len(cleaned):
        a=cleaned[i]
        if (i+1)<len(cleaned):
            b=cleaned[i+1]
            if a==b:
                result+=a+'x'
                i+=1     #remember to update i
            else:
                result+=a+b
                i+=2
        else:
            result+=a+'x'
            i+=1
    return result
    
def pf(text):
    text=pf_prepare(text)    #IMP
    op=""
    for i in range(0,len(text),2):
        a,b=text[i],text[i+1]
        r1,c1,r2,c2=pf_find(pf_key,a,b)
        
        if r1==r2:
            op+=pf_key[r1][(c1+1)%5]
            op+=pf_key[r2][(c2+1)%5]
        elif c1==c2:
            op+=pf_key[(r1+1)%5][c1]
            op+=pf_key[(r2+1)%5][c2]
        else:
            op+=pf_key[r1][c2]
            op+=pf_key[r2][c1]
    return op

def pf_decrypt(text):
    op=""
    for i in range(0,len(text),2):
        a,b=text[i],text[i+1]
        r1,c1,r2,c2=pf_find(pf_key,a,b)
        if r1==r2:
            op+=pf_key[r1][(c1-1)%5]
            op+=pf_key[r2][(c2-1)%5]
        elif c1==c2:
            op+=pf_key[(r1-1)%5][c1]
            op+=pf_key[(r2-1)%5][c2]
        else:
            op+=pf_key[r1][c2]
            op+=pf_key[r2][c1]
    
    return op

#HILL
from sympy import Matrix
hill_key=np.array([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])

inv_hill=np.array(Matrix(hill_key).inv_mod(26))

def hill(text):
    text=text.lower()
    if len(text)%3!=0:
        return "not valid"
    
    result="" 
    for i in range(0,len(text),3):
        block=np.array([[ord(text[i])-97],[ord(text[i+1])-97],[ord(text[i+2])-97]])
        encrypted=(hill_key.dot(block))%26
        for x in encrypted:
            result+=chr(x[0]+97)
    return result

def hill_decrypt(text):
    text=text.lower()
    if len(text)%3!=0:
        return "not valid"
    
    result="" 
    for i in range(0,len(text),3):
        block=np.array([[ord(text[i])-97],[ord(text[i+1])-97],[ord(text[i+2])-97]])
        encrypted=(inv_hill.dot(block))%26
        for x in encrypted:
            result+=chr(x[0]+97)
    return result


#POLY
poly_key="hetanshi"
def poly(text):
    out="" 
    j=0
    for ch in text.lower():
        if 'a'<=ch<='z':
            p=ord(ch)-97
            k=ord(poly_key[j%len(poly_key)])-97    #%len(key)
            out+=chr((p+k)%26+97)
            j+=1  
        else:
            out+=ch
    return out
    
def poly_decrypt(text):
    out=""
    j=0
    for ch in text.lower():
        if 'a'<=ch<='z':   #remember
            c=ord(ch)-97
            k=ord(poly_key[j%len(poly_key)])-97
            out+=chr((c-k+26)%26+97)
            j+=1
        else:
            out+=ch
    return out

def main():
    while True:    # so thar main menu keeps appearing till user exits
        print("\nMAIN MENU")
        print("\n1.Caesar Cipher")
        print("\n2.Monoalphabetic Cipher")
        print("\n3.Playfair Cipher")
        print("\n4.Hill Cipher")
        print("\n5.Polyalphabetic Cipher")
        print("\n6.Exit")

        choice=int(input("Enter choice:"))
        if choice==6:
            break
        text=input("Enter text:")
        if choice == 1:
            key=int(input("Enter Caesar key(integer 0-25)"))
            enc = caesar(text, key)
            print("Encrypted:", enc)
            print("Decrypted:", caesar_decrypt(enc, key))

        elif choice == 2:
            enc = mono(text)
            print("Encrypted:", enc)
            print("Decrypted:", mono_decrypt(enc))

        elif choice == 3:
            enc = pf(text)
            print("Encrypted:", enc)
            print("Decrypted:", pf_decrypt(enc))

        elif choice == 4:
            enc = hill(text)
            print("Encrypted:", enc)
            print("Decrypted:", hill_decrypt(enc))

        elif choice == 5:
            enc = poly(text)
            print("Encrypted:", enc)
            print("Decrypted:", poly_decrypt(enc))

        else:
            print("Invalid")
        
main()
import numpy as np
def euclidean(a,b):
    if a>b:
        r1=a
        r2=b
    else:
        r1=b
        r2=a
    while r2!=0:
        q=r1//r2
        r=r1%r2
        #print(f"{q} | {r1} | {r2} | {r}")
        r1=r2
        r2=r
    return r1

def mi(a,b):
    if a<=b:
        r1=b
        r2=a
    else:
        r1=b
        r2=a%b
    if euclidean(a,b)==1:
        t1=0
        t2=1
        while r2!=0:
            q=r1//r2
            r=r1%r2
            t=t1-t2*q
            r1=r2
            r2=r
            t1=t2
            t2=t
    else:
        print("Numbers are not coprime")
        exit()
    mi=t1
    if mi<=0:
        mi+=b
    return mi

def is_prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0:
        return False
    
    i=3
    while i*i<=n:
        if n%i==0:
            return False
        i+=2
    return True

def choose_e(phi):
        for i in range(3,phi,2): #start from 3, only odd nos for strong and nonproblematic enc
            if euclidean(i,phi)==1:
                return i

def encrypt(M,e,n):
    return pow(M,e,n)

def decrypt(C,d,n):
    return pow(C,d,n)

def rsa(p,q):
    n=p*q
    phi=(p-1)*(q-1)
            
    e=choose_e(phi)
    print(e)
    d=mi(e,phi)
    M=int(input("Enter plaintext:"))
    # or:
    # ch=input("Enter a single character")
    # M=ord(ch)
    
    if M>=n:
        print("Enter a plaintext less than n.\n")
        return
    C=encrypt(M,e,n)
    print("Ciphertext=",C)
    print("Decrypted text=",decrypt(C,d,n))


def main():
    p=int(input("Enter first prime number:"))
    q=int(input("Enter second prime number:"))

    if not is_prime(p) or not is_prime(q):
        print("Enter valid prime numbers.\n")
        exit()
    rsa(p,q)

main()








    

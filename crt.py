import numpy as np
def euclidean(a,b):
    if b==0:
        return a
    else:
        return euclidean(b,a%b)

def mod_inverse(a, m):
    print("a =", a, " m =", m)
    print("--------------------------------------------")
    print("q\t A\t B\t r\t t1\t t2\t t")
    print("--------------------------------------------")

    A = a
    B = m

    # Initial coefficients
    t1 = 0
    t2 = 1

    while B != 0:
        q = A // B
        r = A % B
        t = t1 - q * t2

        print(f"{q}\t {A}\t {B}\t {r}\t {t1}\t {t2}\t {t}")

        # Shift values
        A = B
        B = r
        t1 = t2
        t2 = t

    # A = gcd, t1 = coefficient of original 'a'
    if A != 1:
        print("No inverse exists (gcd =", A, ")")
        return None

    inverse = t1 % m
    print("--------------------------------------------")
    print("Inverse =", inverse)
    print("--------------------------------------------")
    return inverse


def crt(c,m,k):
    M=1 #REMEMBER
    for i in range(0,k):
        M*=m[i]
    M_val=[]
    for i in range(0,k):
        M_val.append(M//m[i])

    M_inv=[]
    for i in range(0,k):
        M_inv.append(mod_inverse(M_val[i],m[i]))

    c_val=0
    print("Residual results:")
    for i in range(0,k):
        print(c[i])
        c_val+=(M_val[i]*M_inv[i]*c[i])%M
    
    return c_val%M #REMEMBER %M again

def main():
    n1=int(input("Enter a:"))
    n2=int(input("Enter b:"))
    k=int(input("How many moduli:"))

    m=[]
    for i in range(0,k):
        m.append(int(input(f'Enter pairwise coprime {i+1}:')))

    a=[]
    b=[]
    for i in range(0,k):
        a.append(n1%m[i])  #MOD m[i]
        b.append(n2%m[i])
    
    choice = int(input('1-Addition\n2-Subtraction\n3-Multiplication\n4-Division'))
    c=[]
    if choice==1:
        for i in range(0,k):
            c.append((a[i]+b[i])%m[i]) #REMEMBER its %m[i]
    elif choice==2:
        for i in range(0,k):
            c.append((a[i]-b[i])%m[i])
    elif choice==3:
        for i in range(0,k):
            c.append((a[i]*b[i])%m[i])
    elif choice==4:
        for i in range(0,k):
            c.append((a[i]*mod_inverse(b[i],m[i]))%m[i])
    else:
        print("Invalid choice")
        exit()
    print(crt(c,m,k))

main()



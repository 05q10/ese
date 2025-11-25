def euclidean(a,b):
    if a<b:
        r1=b
        r2=a
    else:
        r1=a
        r2=b
    while r2!=0:
        q=r1//r2
        r=r1%r2
        print(f"{q} | {r1} | {r2} | {r}")
        r1=r2
        r2=r
    return r1


def extended_euclidean(a,b):
    if a<b:
        r1=b
        r2=a
    else:
        r1=a
        r2=b
    while r2!=0:
        t1=0
        t2=1
        s1=1
        s2=0
        q=r1//r2
        r=r1%r2
        t=t1-t2*q
        s=s1-s2*q
        print(f"{q} | {r1} | {r2} | {r} | {t1} | {t2} | {t} | {s1} | {s2} | {s}")
        r1=r2
        r2=r
        t1=t2
        t2=t
        s1=s2
        s2=s
    return r1

def mi(a,b):
    if a<=b:
        r1=b
        r2=a
    else:
        r1=b
        r2=a%b
    if euclidean(r1,r2)==1: #REMEMBER
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

def main():
    print("q | r1 | r2 | r") #
    print(euclidean(8,12))

    print("q | r1 | r2 | r | t1 | t2 | t | s1 | s2 | s")
    print(extended_euclidean(8,12))

    print("MI of 3,7:")
    print(mi(3,7))



main()
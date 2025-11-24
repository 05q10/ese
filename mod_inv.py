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


# Example Test
mod_inverse(17, 43)

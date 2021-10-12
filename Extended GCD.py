p = 26513
q = 32321

def maths(p, q):
    if p == 0:
        
        return(q, 0, 1)

    else:
        (n, u, v) = maths(q % p, p)
        return(n, v - (q // p) * u, u)

n, u, v = maths(p, q)

print("{}".format(n))
print("{}".format(u))
print("{}".format(v))
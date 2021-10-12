def maths(x, y):
    if x < y:
        
        return maths(y, x)
    
    while y != 0:

        (x, y) = (y, x)

    print("Answer: {}".format(x))
    return x

a = 66528
b = 52920

maths(a, b)

# f = lambda x: x**2 +2
def bissec(f, a , b, tol, n):
    """_summary_

    Args:
        f (_type_): _description_
        a (_type_): _description_
        b (_type_): _description_
        tol (_type_): _description_
        n (_type_): _description_
        x (_type_): _description_
        y (_type_): _description_

    Returns:
        _type_: _description_
    """    
    i = 1
    fa = f(a)
    x = list()
    while(i <= n):
        p = a + (b-a)/2
        fp = f(p)
        x.append(p)
        # parada
        if (fp == 0 or ((b-a)/2<tol)):
            return p, x
        i +=1
        if(fa * fp <= 0):
            b = p
        else:
            a = p
            fa = fp

# print(bissec(f,-10,10,10**-2,100))

def solve_tridiagonal(A, d):
    n = len(d)
    c, b, x = [0] * n, [0] * n, [0] * n

    c[0] = A[0][1] / A[0][0]
    for i in range(1, n-1):
        c[i] = A[i][i+1] / (A[i][i] - A[i][i-1] * c[i-1])

    b[0] = d[0] / A[0][0]
    for i in range(1, n):
        b[i] = (d[i] - A[i][i-1] * b[i-1]) / (A[i][i] - A[i][i-1] * c[i-1])

    x[n-1] = b[n-1]
    for i in range(n-2, -1, -1):
        x[i] = b[i] - c[i] * x[i+1]

    return x
from math import sin, cos
from os import system

A = B = 0

system('cls')
while True:
    b = [' '] * 1760
    z = [0] * 1760 

    j = 0
    while j < 6.28:
        i = 0
        while i < 6.28:
            c, d, e, f, g = sin(i), cos(j), sin(A), sin(j), cos(A)

            h = d + 2
            D = 1 / (c * h * e + f * g + 5)

            l, m, n = cos(i), cos(B), sin(B)

            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = x + 80 * y
            
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))

            if 0 < y < 22 and 0 < x < 80 and z[o] < D:
                z[o] = D
                b[o] = '.,-~:;=!*#$@'[N if N > 0 else 0]

            i += 0.02
        j += 0.07
    
    w = '\n'.join([''.join(b[k:(k + 80)]) for k in range(0, 1761, 80)])
    system('cls')
    print(w)

    A += 0.0704
    B += 0.0352

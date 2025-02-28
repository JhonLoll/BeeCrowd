#? QUESTÕES RESOLVIDAS MATH
# BEE1093

def BEE1093():
    caso = int(input())
    x = 4
    while caso > 0:

        a, b = input().split(" ")

        a = int(a)
        b = int(b)

        while True:
            if a % x == 0 and b % x == 0:
                print(x)
                break
            x += 1

        caso -= 1
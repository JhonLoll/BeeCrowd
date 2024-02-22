
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
        
def BEE109x():
    zero, one, two, three, four, five, six, seven, eight, nine = (0,0,0,0,0,0,0,0,0,0)
    while True:
        
        a, b = input().split(" ")
        a = int(a)
        b = int(b)
        
        if a == 0 and b == 0:
            break
        
        for i in range(a, b + 1):
            for x in str(i):
                match x:
                    case '0':
                        zero += 1
                    case '1':
                        one += 1
                    case '2':
                        two += 1
                    case '3':
                        three += 1
                    case '4':
                        four += 1
                    case '5':
                        five += 1
                    case '6':
                        six += 1
                    case '7':
                        seven += 1
                    case '8':
                        eight += 1
                    case '9': 
                        nine += 1
                        
        print(f'{zero} {one} {two} {three} {four} {five} {six} {seven} {eight} {nine}')    
        


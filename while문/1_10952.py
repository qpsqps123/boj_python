import sys
while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        if A > 0 and B < 10:
            print(A + B)
        else:
            break
    except:
        break

import sys
N = int(sys.stdin.readline())
if(N>0 and N<=100000):
    for i in range(1, N+1):
        print(i)
else:
    print('N의 범위는 1~100000입니다.')

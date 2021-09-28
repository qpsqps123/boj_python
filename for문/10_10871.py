import sys
while True:
    try:
        N, X = map(int, sys.stdin.readline().split())
        if type(N) == int and type(X) == int and N >= 1 and N <= 10000 and X >= 1 and X <= 10000:
            while True:
                try:
                    A = list(map(int, sys.stdin.readline().split()))
                    if type(len(A)) == int and len(A) == N:
                        for i in range(len(A)):
                             if A[i] < X:
                                  print(A[i], end = ' ')
                        break
                    elif len(A) != N:
                        print('정확한 개수를 입력하세요.')
                except ValueError:
                    print('입력한 값이 정수가 아닙니다.')
            break
        elif N < 1 or N > 10000 or X < 1 or X > 10000:
           print('범위는 1~10000 입니다.')
    except ValueError:
        print('입력한 값이 정확한 개수가 아니거나 정수가 아닙니다.')

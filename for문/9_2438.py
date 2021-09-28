N = int(input())
if(N >= 1 and N <=100):
    for i in range(1, N+1):
        print(' ' * (N-i), '*' * i, sep = '')
else:
    print('N의 범위는 1~100 입니다.')

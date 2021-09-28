import sys
T = int(sys.stdin.readline())
for i in range(T):
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    if(A > 0 and B < 10):
        print('Case #', i+1, ': ', A, ' + ', B, ' = ', A+B, sep = '')
    else:
        print('A > 0, B < 10 이어야 합니다.')

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
if(A < 2 or B < 2 or C < 2 or A > 10000 or B > 10000 or C > 10000):
    print('잘못된 입력입니다.')
else:
    print((A+B)%C), print(((A%C)+(B%C))%C), print((A*B)%C), print((A%C)*(B%C)%C)

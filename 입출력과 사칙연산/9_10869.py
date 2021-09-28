A, B = input().split()
A = int(A)
B = int(B)
if(A < 1 or B < 1 or B > 10000):
    print('잘못된 입력입니다')
else:print(A+B), print(A-B), print(A*B), print(int(A/B)), print(A%B)

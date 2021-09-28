A = input()
B = input()
A = int(A)
B = int(B)
C = B/100
D = (B%100)/10
E = B%10
C = int(C)
D = int(D)
E = int(E)
if(A < 1 or B < 1):
    print('자연수를 입력해주세요.')
else:
    print(A*E), print(A*D), print(A*C), print((A*E)+((A*D)*10)+((A*C)*100))

T = int(input())
for i in range(T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    if(A>0 and B<10):
        print(A+B)
    else:
        print('A>0, B<10인 정수값을 입력해주세요.')

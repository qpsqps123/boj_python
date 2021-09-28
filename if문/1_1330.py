A, B = input().split()
A = int(A)
B = int(B)

if(A<-10000 or B<-10000 or A>10000 or B>10000):
    print('-10000부터 10000사이의 정수를 입력해주세요.')
elif(A>B):
    print('>')
elif(A<B):
    print('<')
elif(A==B):
    print('==')

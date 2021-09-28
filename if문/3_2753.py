A = input()
A = int(A)
if(A<0 or A>4000):
    print('연도의 범위는 1~4000입니다.')
elif((A%4)==0 and ((A%100)!=0) or ((A%400)==0)):
    print('1')
else:
    print('0')

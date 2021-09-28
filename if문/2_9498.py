A = input()
A = int(A)
if(A<0 or A>100):
    print('점수범위는 0~100입니다')
elif(A>=90 and A<=100):
    print('A')
elif(A>=80 and A<90):
    print('B')
elif(A>=70 and A<80):
    print('C')
elif(A>=60 and A<70):
    print('D')
else:
    print('F')

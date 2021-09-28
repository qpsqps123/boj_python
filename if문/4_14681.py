x = input()
y = input()
x = int(x)
y = int(y)
if(x<-1000 or x>1000 or x==0 or y<-1000 or y>1000 or y==0):
    print('x와 y의 범위는 -1000~1000이며, 0은 포함되지 않습니다.')
elif(x>0 and y>0):
    print('1')
elif(x<0 and y>0):
    print('2')
elif(x<0 and y<0):
    print('3')
elif(x>0 and y<0):
    print('4')

H, M = input().split()
H = int(H)
M = int(M)
if(H<0 or H>23 or M<0 or M>59):
    print('H의 범위는 0~23이고 M의 범위는 0~59입니다.')
elif(H==0 and M>=0 and M<45):
    print(H+23, M+15)
elif(H>0 and H<24 and M>=0 and M<45):
    print(H-1, M+15)
elif(H>=0 and M>=45 and M<60):
    print(H, M-45)


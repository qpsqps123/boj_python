import sys
while True:
    try:
        A = int(sys.stdin.readline())
        if A >= 0 and A <=99:
            C = A % 10                  ## C = A의 1의 자리(The ones place of number A)
            B = (A - (A % 10)) / 10     ## B = A의 10의 자리(The tens place of number A)
            D = B + C                   ## D = B(A의 10의 자리)와 C(A의 1의 자리)의 합(The sum of B and C)
            E = (C * 10)+(D % 10)       ## E = 새로운 수(New Number, C is going to be the tens place of E, and D is going to be the ones place of the new number)
            B = E
            F = 1
            if B == A:
                break
            else:
                F = F + 1
                break
        else:
            print('입력 가능한 수의 범위는 0~99 입니다.')    ## 바로 강제종료 원할시 sys.exit(1) 사용 (If you want to make it exited, use the code 'sys.exit(1)')
    except ValueError:
        print('0~99 사이의 정수만 입력 가능합니다.')         ## 바로 강제종료 원할시 sys.exit(1) 사용 (If you want to make it exited, use the code 'sys.exit(1)')
while True:
    C = B % 10                  ## C = 이전 B의 1의 자리(The ones place of old B)
    B = (B - (B % 10)) / 10     ## 새로운 B(New B) = 이전 B의 10의 자리(The tens place of old B)
    D = B + C                   ## D = 새로운 B(이전 B의 10의 자리)와 C(이전B의 1의 자리)의 합(The sum of New B and C)
    E = (C * 10) + (D %  10)    ##  E = 새로운 수(New Number, C is going to be the tens place of E, and D is going to be the ones place of the new number)
    B = E
    if B == A:
        print(F)
        break
    else:
        F = F+1

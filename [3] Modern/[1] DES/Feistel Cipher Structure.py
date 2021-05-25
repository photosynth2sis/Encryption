# 페이스텔 암호 구조

# 자세한 것은 사진 참조

# 이산연산을 XOR(DES와 동일)이라고 가정 (GF(2)에서의 덧셈)

'''
기본구조:
L(i) = R(i-1)
R(i) = L(i-1) ■ f(R(i-1), K(i)) | ■ : XOR 연산
'''



def BasicSetting():
    global L,R,Ltemp,Rtemp,Key
    global n,n2
    n = len(Subject)
    n2 = int(len(Subject) / 2)
    # Key | 010001
    Key = [0,1,0,0,0,1]
    # L, R, temp
    L = [0] * n2
    R = [0] * n2
    Ltemp = [0] * n2
    Rtemp = [0] * n2
    for i in range(0,n2):
        L[i] = int(Subject[i])
        R[i] = int(Subject[i+n2])




def Encrypt(L,R,L2,R2,Key):
    for i in range(RoundTime * 2):
        for j in range(0,n2):
            # 에러 확인용
            #print(L,R,L2,R2,i%6)

            L2[j] = R[j]
            R2[j] = L[j] ^ (R[j] | Key[i%6])
            if i != RoundTime*2-1:
                R[j] = R2[j]
                L[j] = L2[j]
            else:
                L[j] = R2[j]
                R[j] = L2[j]

               # print("adsfdkfjdklflj")

        #print("---------------------------------")

    for i in range(0, n2):
        print(L[i], end='')
    for i in range(0, n2):
        print(R[i], end='')
    print()



def Decrypt(L,R,L2,R2,Key):
    for i in range(RoundTime * 2):
        for j in range(0,n2):

            # 에러 확인용
            #print(L,R,L2,R2,((6-(6-RoundTime*2)%6)-1-i)%6)

            L2[j] = R[j]
            R2[j] = L[j] ^ ( R[j] | Key[((6-(6-RoundTime*2)%6)-1-i)%6] )

            if i != RoundTime*2-1:
                R[j] = R2[j]
                L[j] = L2[j]
            else:
                L[j] = R2[j]
                R[j] = L2[j]

        # 에러 확인용
        #print("---------------------------------")

    for i in range(0, n2):
        print(L[i], end='')
    for i in range(0, n2):
        print(R[i], end='')
    print()



# Main 코드실행구간

OddCheck = 0
while True:
    EorD = int(input("암호화(0) / 복호화(1) 중 선택하세요:"))
    print("0/1(bit) 암호화를 진행합니다"if EorD==0 else("0/1(bit) 복호화를 진행합니다"))

    while OddCheck == 0:
        InputStr = input("짝수 개의 0/1(bit)를 입력해주세요:")
        Subject = list(InputStr)
        if len(Subject)%2 != 0:
            print("홀수 개를 입력하셨습니다. 다시 입력해주세요.")
            continue
        else:
            OddCheck = 1

    OddCheck = 0
    RoundTime = int(input("Round 진행횟수를 입력하세요. 2n회만큼 진행합니다. : "))
    A = BasicSetting()

    if EorD == 0:
        Encrypt(L,R,Ltemp,Rtemp,Key)
    elif EorD == 1:
        Decrypt(L,R,Ltemp,Rtemp,Key)

    L = [0]
    R = [0]
    Ltemp = [0]
    Rtemp = [0]
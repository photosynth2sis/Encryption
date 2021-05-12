# 비즈네르 암호

def ListPrepare(Key):

    global LS, LK
    global OrdSub, OrdKey

    # Key의 리스트화 작업
    LK = len(Key)
    OrdKey = [0] * LK
    for i in range(0,LK):
        OrdKey[i] = ord(Key[i])

    # 암호화 / 복호화 대상의 리스트화 작업
    LS = len(Subject)
    OrdSub = [0] * LS
    for j in range(0,LS):
        OrdSub[j] = ord(Subject[j])

    # 문제 확인용
    #print(OrdSub)
    #print(OrdKey)

def Encryption():
    SubCount = 0
    Breaker = 0
    while SubCount <= LS:
        for i in range(0,LK):
            # 리스트 범위 초과 방지
            if SubCount == LS:
                Breaker = 1
                break
            # 암호화
            if 65 <= OrdSub[SubCount] <= 90 and 65 <= OrdKey[i] <= 90:
                OrdSub[SubCount] = ( (OrdSub[SubCount])-65 + OrdKey[i]-65 ) % 26 + 65
            elif 65 <= OrdSub[SubCount] <= 90 and 97 <= OrdKey[i] <= 122:
                OrdSub[SubCount] = ( (OrdSub[SubCount])-65 + OrdKey[i]-97 ) % 26 + 65
            elif 97 <= OrdSub[SubCount] <= 122 and 65 <= OrdKey[i] <= 90:
                OrdSub[SubCount] = ( (OrdSub[SubCount])-97 + OrdKey[i]-65 ) % 26 + 97
            elif 97 <= OrdSub[SubCount] <= 122 and 97 <= OrdKey[i] <= 122:
                OrdSub[SubCount] = ( (OrdSub[SubCount])-97 + OrdKey[i]-97) % 26 + 97
            # 문제 확인용
            #print(SubCount)
            SubCount += 1

        if Breaker == 1: # 리스트 범위 초과시 while문도 break
            break
        i = 0
    # 문자로 바꾸기
    for j in range(0,LS):
        Subject[j] = chr(OrdSub[j])
        print(Subject[j],end='')

    # 문제 확인용
    #print(OrdSub)

def Decryption():
    SubCount = 0
    Breaker = 0
    while SubCount <= LS:
        for i in range(0,LK):
            # 리스트 범위 초과 방지
            if SubCount == LS:
                Breaker = 1
                break
            # 암호화
            if 65 <= OrdSub[SubCount] <= 90 and 65 <= OrdKey[i] <= 90:
                OrdSub[SubCount] = ( (OrdSub[SubCount])-65 - OrdKey[i]+65 ) % 26 + 65
            elif 65 <= OrdSub[SubCount] <= 90 and 97 <= OrdKey[i] <= 122:
                OrdSub[SubCount] = ( (OrdSub[SubCount])-65 - OrdKey[i]+97 ) % 26 + 65
            elif 97 <= OrdSub[SubCount] <= 122 and 65 <= OrdKey[i] <= 90:
                OrdSub[SubCount] = ( (OrdSub[SubCount])-97 - OrdKey[i]+65 ) % 26 + 97
            elif 97 <= OrdSub[SubCount] <= 122 and 97 <= OrdKey[i] <= 122:
                OrdSub[SubCount] = ( (OrdSub[SubCount])-97 - OrdKey[i]+97) % 26 + 97
            # 문제 확인용
            #print(SubCount)
            SubCount += 1

        if Breaker == 1: # 리스트 범위 초과시 while문도 break
            break
        i = 0
    # 문자로 바꾸기
    for j in range(0,LS):
        Subject[j] = chr(OrdSub[j])
        print(Subject[j],end='')

    # 문제 확인용
    #print(OrdSub)





while True:
    print("비즈네르 암호 프로그램입니다.")
    EorD = int(input("암호화(0) / 복호화(1) 중 선택하세요:"))
    Subject = list(input("암호화할 문장을 입력하세요:" if EorD == 0 else("복호화할 문장을 입력하세요:")))
    print("Key값은 대소문자에 영향을 받지 않으며, 숫자의 경우 암호화가 진행되지 않습니다.")
    Key = list(input("Key값을 입력해주세요:"))

    ListPrepare(Key)
    if EorD == 0:
        Encryption()
    else:
        Decryption()
    print()
    print()
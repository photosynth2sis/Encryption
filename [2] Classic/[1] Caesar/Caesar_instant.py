# 카이사르 암호화
# 영어 문자(ASCHII 65~90, 97~122)의 경우에만 문자열 Shift 진행


def encryption(key):
    n = len(S)
    P = list(S)
    aP = [0] * n
    Enct = [0] * n
    Enc = [0] * n
    for i in range(0,n):
        aP[i] = ord(P[i])
    for j in range(0,n):
        if 65 <= aP[j] <= 90:
            Enct[j] = (aP[j] - 65 + key) % 26 + 65
        elif 97 <= aP[j] <= 122:
            Enct[j] = (aP[j] - 97 + key) % 26 + 97
        else:
            Enct[j] = aP[j]
    for k in range(0,n):
        Enc[k] = chr(Enct[k])
        print(Enc[k],end='')
    print()
    print()


def decryption(key):
    n = len(S)
    P = list(S)
    aP = [0] * n
    Dect = [0] * n
    Dec = [0] * n
    for i in range(0,n):
        aP[i] = ord(P[i])
    for j in range(0,n):
        if 65 <= aP[j] <= 90:
            Dect[j] = (aP[j] - 65 - key) % 26 + 65
        elif 97 <= aP[j] <= 122:
            Dect[j] = (aP[j] - 97 - Key) % 26 + 97
        else:
            Dect[j] = aP[j]
    for k in range(0,n):
        Dec[k] = chr(Dect[k])
        print(Dec[k],end='')
    print()
    print()


while True:
    EorD = input("암호화(0), 복호화(1) 중 옵션을 선택하세요:")

    if EorD == '0':
        S = input("암호화할 문장을 입력해주세요:")
        Key = int(input("암호화를 위한 Key값을 입력해주세요:"))
        encryption(Key)
    else:
        S = input("복호화할 문장을 입력해주세요:")
        Key = int(input("복호화를 위한 Key값을 입력해주세요:"))
        decryption(Key)
# 카이사르 암호화
# 영어 문자(ASCHII 65~90, 97~122)의 경우에만 문자열 Shift 진행

def encryption(Key):
    Sub = open("Caesar.txt",'r') # 텍스트 파일 열기
    LineRead = Sub.readlines() # 리스트로 모든 줄 읽기
    ExStr = [0] * len(LineRead) # 리스트의 len(몇줄인지 알아냄)
    for i in range (0,len(LineRead)-1):
        a = LineRead[i] # 각줄마다 작용
        ExStr[i] = a[0:len(a)-1] # 맨 마지막 \n문자 지워서 ExStr에 대입
    ExStr[len(LineRead)-1] = LineRead[len(LineRead)-1]
    Sub.close()

    EachStr = [0] * len(LineRead) # 문자 하나하나를 저장하기 위함

    for j in range(0,len(LineRead)): # 문자 하나하나 / 각 줄을 저장하는 리스트 만들기
        EachStr[j] = list(ExStr[j])


    Ord = []
    for ii in range(0,len(LineRead)): # Ord정보 저장할 빈 이차원배열
        OLine = []
        for jj in range(0,len(EachStr[ii])):
            OLine.append(0)
        Ord.append(OLine)

    for k in range(0,len(LineRead)): # 빈 이차원배열 Ord에 EachStr의 Ord값을 집어넣음
        for l in range(0,len(EachStr[k])):
            Ord[k][l] = ord(EachStr[k][l])


    for l in range(0,len(LineRead)): # ord상태에서의 shift(암호화/복호화)
        for m in range(0,len(Ord[l])):
            if 65 <= Ord[l][m] <= 90:
                Ord[l][m] = (Ord[l][m] - 65 + Key) % 26 + 65
            elif 97 <= Ord[l][m] <= 122:
                Ord[l][m] = (Ord[l][m] - 97 + Key) % 26 + 97

    Fin = []
    for ii in range(0,len(LineRead)): # Ord정보 저장할 빈 이차원배열
        OLine = []
        for jj in range(0,len(EachStr[ii])):
            OLine.append("")
        Fin.append(OLine)

    for n in range(0,len(LineRead)):
        for p in range(0,len(EachStr[n])):
            Fin[n][p] = chr(Ord[n][p])

    Wri = open("Encrypted.txt","w") # 작성을 위한 파일 열기

    Final = [""] * len(LineRead)

    for q in range(0,len(LineRead)):
        temp = ''
        for r in range(0,len(EachStr[q])):
            temp += Fin[q][r]
            Final[q] = temp

    for r in range(0,len(LineRead)):
        Wri.write(Final[r])
        Wri.write("\n")


def decryption(Key):
    Sub = open("Caesar.txt",'r') # 텍스트 파일 열기
    LineRead = Sub.readlines() # 리스트로 모든 줄 읽기
    ExStr = [0] * len(LineRead) # 리스트의 len(몇줄인지 알아냄)
    for i in range (0,len(LineRead)-1):
        a = LineRead[i] # 각줄마다 작용
        ExStr[i] = a[0:len(a)-1] # 맨 마지막 \n문자 지워서 ExStr에 대입
    ExStr[len(LineRead)-1] = LineRead[len(LineRead)-1]
    Sub.close()

    EachStr = [0] * len(LineRead) # 문자 하나하나를 저장하기 위함

    for j in range(0,len(LineRead)): # 문자 하나하나 / 각 줄을 저장하는 리스트 만들기
        EachStr[j] = list(ExStr[j])


    Ord = []
    for ii in range(0,len(LineRead)): # Ord정보 저장할 빈 이차원배열
        OLine = []
        for jj in range(0,len(EachStr[ii])):
            OLine.append(0)
        Ord.append(OLine)

    for k in range(0,len(LineRead)): # 빈 이차원배열 Ord에 EachStr의 Ord값을 집어넣음
        for l in range(0,len(EachStr[k])):
            Ord[k][l] = ord(EachStr[k][l])


    for l in range(0,len(LineRead)): # ord상태에서의 shift(암호화/복호화)
        for m in range(0,len(Ord[l])):
            if 65 <= Ord[l][m] <= 90:
                Ord[l][m] = (Ord[l][m] - 65 - Key) % 26 + 65
            elif 97 <= Ord[l][m] <= 122:
                Ord[l][m] = (Ord[l][m] - 97 - Key) % 26 + 97

    Fin = []
    for ii in range(0,len(LineRead)): # Ord정보 저장할 빈 이차원배열
        OLine = []
        for jj in range(0,len(EachStr[ii])):
            OLine.append("")
        Fin.append(OLine)

    for n in range(0,len(LineRead)):
        for p in range(0,len(EachStr[n])):
            Fin[n][p] = chr(Ord[n][p])

    Wri = open("Decrypted.txt","w") # 작성을 위한 파일 열기

    Final = [""] * len(LineRead)

    for q in range(0,len(LineRead)):
        temp = ''
        for r in range(0,len(EachStr[q])):
            temp += Fin[q][r]
        Final[q] = temp

    for r in range(0,len(LineRead)):
        Wri.write(Final[r])
        Wri.write("\n")


print("파일의 카이사르 암호화/복호화 프로그램입니다. 해당 경로에 'Caesar.txt' 파일이 필요합니다.")
EorD = input("암호화(0), 복호화(1) 중 옵션을 선택하세요:")
if EorD == '0':
    Key = int(input("암호화를 위한 Key값을 입력해주세요:"))
    encryption(Key)
    print("Encrypted.txt에 암호화 완료")
elif EorD == '1':
    Key = int(input("복호화를 위한 Key값을 입력해주세요:"))
    decryption(Key)
    print("Decrypted.txt에 복호화 완료")
# 전치 암호 | 문자의 배열을 바꾸는 방식

'''
d = 6

[암호화]
암호 위치 | 1 | 2 | 3 | 4 | 5 | 6 |
평문 위치 | 3 | 5 | 1 | 6 | 4 | 2 |

[복호화]
평문 위치 | 1 | 2 | 3 | 4 | 5 | 6 |
암호 위치 | 3 | 5 | 1 | 6 | 4 | 2 |

'''

EKey = [3,5,1,6,4,2]
DKey = [3,6,1,5,2,4]


# Subject의 요소 개수를 Key의 배수로 맞춤(6n개)
def Listappend():
    if len(Subject) % 6 != 0:
        for i in range(0,6):
            Subject.append("_")
            if len(Subject) % 6 == 0:
                break





def Encryption():
    Encrypted = ["NULL"] * len(Subject)

    # 오류 확인용
    #print(Subject)
    #print(Encrypted)


    for i in range(0,len(Subject)):
        Encrypted[i] = Subject[i//6 + (EKey[i%6]-1)]

    for j in range(0,len(Encrypted)):
        if Encrypted[j] != "NULL":
            print(Encrypted[j],end='')

    print()
    print()

def Decryption():
    Decrypted = ["NULL"] * len(Subject)

    # 오류 확인용
    #print(Subject)
    #print(Encrypted)


    for i in range(0,len(Subject)):
        Decrypted[i] = Subject[i//6 + (DKey[i%6]-1)]

    for j in range(0,len(Decrypted)):
        if Decrypted[j] != "NULL":
            print(Decrypted[j],end='')

    print()
    print()


while True:
    print("전치 암호 프로그램입니다.")
    print("암호화 / 복호화 키는 다음과 같습니다.")
    print(" [암호화] \t\t\t\t\t\t\t\t\t\t [복호화]")
    print(" 기본평문 위치 : | 1 | 2 | 3 | 4 | 5 | 6 |\t\t 암호화된 위치 : | 1 | 2 | 3 | 4 | 5 | 6 |" ,"\n", "\r 암호회된 위치 : | 3 | 5 | 1 | 6 | 4 | 2 |\t\t 복호화된 위치 : | 3 | 6 | 1 | 5 | 2 | 4 |")
    EorD = int(input("암호화(0) / 복호화(1) 중 선택하세요:"))
    print('대칭성을 위해 맨 마지막 절에 "_"가 일부 추가될 수 있습니다.')
    Subject = list(input("암호화할 문장을 입력하세요:" if EorD == 0 else("복호화할 문장을 입력하세요:")))

    if EorD == 0:
        Listappend()
        Encryption()
    elif EorD == 1:
        Listappend()
        Decryption()
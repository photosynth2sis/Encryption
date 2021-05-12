# 유클리드 호제법_확장

# 특수상황 - 잉여역수(곱셈의 역원) 구하기

n = input("법 a에 대한 b의 잉여역수를 구하는 프로그램입니다. :").split()
a = int(n[0])
b = int(n[1]) - (int(n[1]) // int(n[0])) * int(n[0])


def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a



def inverse(a,b):
    t1 = 0
    t2 = 1
    while b != 0:
        q = a // b
        r = a % b
        t = t1 - t2*q

        a = b
        b = r
        t1 = t2
        t2 = t

    return t1


if gcd(a,b) == 1:
    print("%d + %d*n" %(inverse(a,b), a))
else:
    print("a와 b가 서로소가 아니기에 잉여역수가 존재하지 않습니다.")
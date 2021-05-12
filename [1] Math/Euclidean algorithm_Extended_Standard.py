# 유클리드 호제법_확장

# 일반적 상황 - 1차 디오판틴 방정식의 해 구하기

n = input("1차 디오판틴 방정식 [a*s + b*t = gcd(a,b)]의 해를 구하는 프로그램입니다. :").split()
a = int(n[0])
b = int(n[1])


def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def Diophantine(a,b):
    global s1
    global t1
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while b != 0:
        q = a // b
        r = a % b
        s = s1 - s2*q
        t = t1 - t2*q

        a = b
        b = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t

    return s1, t1


print("a=",a,"/","b=",b,"//","gcd(a,b)=",gcd(a,b))
print("%d*%d + %d*%d = %d" % (a, Diophantine(a,b)[0], b, Diophantine(a,b)[1], gcd(a,b)))
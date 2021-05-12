# 유클리드 호제법_기본

# 두 수의 최대공약수를 구하는 알고리즘

n = input("최소공배수를 구할 2개의 숫자를 적어주세요.:").split()

a = int(n[0])
b = int(n[1])

if a < b:
    a,b = b,a

def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

print(gcd(a,b))
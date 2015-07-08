#最大公约数gcd(a, b)
def gcd(a,b):
    return a if b ==0 else gcd(b, a%b)

#最小公倍数lcm(a, b)
def lcm(a,b):
    return a * b / gcd(a, b)

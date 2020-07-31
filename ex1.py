def gcd(a,b):
    if a % b == 0:
        return b
    return(gcd(b,a%b))

def fraction(a,b):
    return str(int(a/gcd(a,b))) + "/" + str(int(b/gcd(a,b)))

# print(gcd(200,150))
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

while b == 0:
    b = int(input("Nhap lai b: "))

print(gcd(a,b))
print(fraction(a,b))
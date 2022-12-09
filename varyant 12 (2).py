import math
def med(a,b,c):
    med=math.sqrt(2*(b*b+c*c)-a*a)/2
    return med
print("Enter the sides of the triangle:")
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
if abs(a-b)>=c | a+b<=c:
    print("It's not a triangle")
print("Medians of the original triangle:")
ma=med(a, b, c)
mb=med(b, a, c)
mc=med(c, a, b)
print("1-i median", ma, "\t2-i median", mb, "\t3-i median", mc)
print("Required medians:")
mma=med(ma, mb, mc)
mmb=med(mb, ma, mc)
mmc=med(mc, ma, mb)
print("1-i median", mma, "\t2-i median", mmb, "\t3-i median", mmc)
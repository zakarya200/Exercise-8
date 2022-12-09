def primes(n):
    b=[True]*n 
    for i in range(3, int(n**0.5)+1, 2):
        if b[i]:
            b[i*i:2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2]+[i for i in range(3, n, 2) if b[i]] 
def b(num, ans):
    delit = 1
    for j in range(len(ans)):
        i = 0
        while not num % ans[j]:
            num //= ans[j]
            i+=1
        if i:
            delit*=i+1
        if num < ans[j] * ans[j] :
            break
    if num - 1:
        delit*=2
    return delit


def main(m, n):
    max=0
    a = primes(int(n**0.5)+1)
    for i in range(m, n+1):
        k = b(i, a)
        if k > max:
            max = k 
            res = i 
    return res 
 
print(main(1000, 500000))
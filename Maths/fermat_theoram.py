# program to find modulas multiplicative inverse of "a" under "m" when m is prime using fetmat's theoram

def mod_in(a,m):
    return pow(a,m-2,m)

a,m = map(int,input().split())
print(mod_in(a,m))
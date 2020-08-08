s = input()
prod = 1
for i in range(13):
    prod *= int(s[i])
mx = prod
for i in range(13,len(s)):
    if int(s[i-13]) != 0:
        prod = (prod//int(s[i-13])) * int(s[i]) 
        mx = max(mx,prod)
    else:
        prod = prod * int(s[i])
print(mx)
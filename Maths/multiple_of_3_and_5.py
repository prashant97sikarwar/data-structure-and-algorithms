sm = 0
i = 3
while i <= 999:
    if i % 3 == 0:
        sm += i
    i += 3
j = 5
while j <= 995:
    if j % 5 == 0:
        sm += j
    j += 5
    
k = 15
while k <= 990:
    if k % 15 == 0:
        sm -= k
    k += 15
print(sm)
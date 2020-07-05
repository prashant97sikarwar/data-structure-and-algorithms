s = input()
n = int(input())
s = list(s)
for i in range(len(s)):
    if s[i].isalnum():
        if s[i].isdigit():
            s[i] = str((int(s[i]) + n) % 10)
        elif s[i].isupper():
            if ord(s[i]) + n%26 > 90:
                s[i] = chr(((n % 26) + ord(s[i])) % 90 + 64)
            else:
                s[i] = chr(ord(s[i]) + (n % 26))
        else:
            if ord(s[i]) + n%26 > 122:
                s[i] = chr((((n % 26) + ord(s[i])) % 122) + 96)
            else:
                s[i] = chr(ord(s[i]) + (n % 26))
print(''.join(s))
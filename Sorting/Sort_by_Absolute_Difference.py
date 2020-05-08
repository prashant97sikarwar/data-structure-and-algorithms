for _ in range(int(input())):
    n,k=map(int,input().split())
    print(*sorted(list(map(int,input().split())),key=lambda x:abs(x-k)))
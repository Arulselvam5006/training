a=int(input())
s=list(map(int,input().split()[:a]))
s.sort()
for i in s:
    print(i,end=" ")

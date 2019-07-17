a=int(input())
h=list(map(int,input().split()[:a]))
h.sort()
for i in h:
  print(i,end="")

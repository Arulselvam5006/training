r=int(input())
asm=list(map(int,input().split()))
m=sorted(asm)
print(m[r//2])

r1,r2=map(int,input().split())
for r in range(r1+1,r2):
 sum=0
 temp=r
 while temp>0:
  digit=temp%10
  sum+=digit**3
  temp//=10
 if r==sum:
    print(r,end=" ")
  

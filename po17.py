a = input()
b = len(a)
c = 0
for i in a:
  i = int(i)
  c += pow(i,b)
if c == int(a):
  print("yes")
else:
  print("no")

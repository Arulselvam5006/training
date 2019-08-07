#a
s1=list(input())
s2=" "
for i in range(len(s1)):
    if s2 in s1:
        s1.remove(s2)
print(len(s1))

now=0
s=[2021]*10
print(s)
flag=1
while flag:
  now+=1
  cop=now
  while cop>0:
    curr=cop%10
    s[curr]-=1
    if s[curr]<0:
      flag=0
      break
    cop//=10
print(now-1)
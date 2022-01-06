n=int(input())
s=[[0]*(n+1) for i in range(n+1)]
s[1][n//2+1]=1
pntx,pnty=1,n//2+1
for k in range(2,n*n+1):
  if pntx==1 and pnty!=n:
    s[n][pnty+1]=k
    pntx=n; pnty+=1
  elif pntx!=1 and pnty==n:
    s[pntx-1][1]=k
    pntx-=1; pnty=1
  elif pntx==1 and pnty==n:
    s[pntx+1][pnty]=k
    pntx+=1
  elif pntx!=1 and pnty!=n:
    if s[pntx-1][pnty+1]==0:
      s[pntx-1][pnty+1]=k
      pntx-=1; pnty+=1
    else:
      s[pntx+1][pnty]=k
      pntx+=1
for i in range(1,n+1):
  for j in range(1,n+1):
    print(s[i][j],end=' ')
  print()
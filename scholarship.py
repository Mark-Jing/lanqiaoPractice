n=int(input())
stu=[]
for i in range(1,n+1):
  chi,ma,en=map(int,input().split())
  stu.append([i,chi,ma,en,chi+ma+en])
stu.sort(key=lambda s:(s[4],s[1]),reverse=True)
for i in range(5):
  print(stu[i][0],stu[i][4])
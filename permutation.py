def dfs(x):
    if x==n+1:
        for i in range(1,n):
            print(a[i],end=' ')
        print(a[n])
    for i in range(1,n+1):
        if not vis[i]:
            a[x]=i; vis[i]=1
            dfs(x+1)
            vis[i]=0

n=int(input())
vis=[0]*(n+1)
a=[0]*(n+1)
dfs(1)
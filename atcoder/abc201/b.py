N = int(input())
ST = [list(input().split()) for _ in range(N)]
ST.sort(key=lambda x: int(x[1]), reverse=True)
print(ST[1][0])

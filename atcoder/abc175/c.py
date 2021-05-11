X,K,D = map(int, input().split())

n = max(0, (D * K - X) // (2 * D))
n = min(n, K-1)
ans = min( abs(X-D*K+2*D*n), abs(X-D*K+2*D*(n+1)))
print(ans)

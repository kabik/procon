S = input()

ans = 10**10
for i in range(len(S)-2):
    n = int(S[i:i+3])
    ans = min(ans, abs(753-n))
print(ans)

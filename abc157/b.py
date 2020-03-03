A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

def is_bingo(A, B):
    if A[0][0] in B and A[0][1] in B and A[0][2] in B:
        return True
    if A[1][0] in B and A[1][1] in B and A[1][2] in B:
        return True
    if A[2][0] in B and A[2][1] in B and A[2][2] in B:
        return True

    if A[0][0] in B and A[1][0] in B and A[2][0] in B:
        return True
    if A[0][1] in B and A[1][1] in B and A[2][1] in B:
        return True
    if A[0][2] in B and A[1][2] in B and A[2][2] in B:
        return True

    if A[0][0] in B and A[1][1] in B and A[2][2] in B:
        return True
    if A[0][2] in B and A[1][1] in B and A[2][0] in B:
        return True

    return False

print('Yes' if is_bingo(A, B) else 'No')

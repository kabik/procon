"""
import sys
input = sys.stdin.readline

AB = input().split()
A = int(AB[0])
B100 = round(float(AB[1])*100)

print( A*B100//100 )
"""

import decimal
AB = input().split()
A = decimal.Decimal(AB[0])
B = decimal.Decimal(AB[1])
print(int(A*B))

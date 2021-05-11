s = input()
l = [s for s,t in zip(s,s[1:]) if s==t]
print('Bad' if len(l) else 'Good')

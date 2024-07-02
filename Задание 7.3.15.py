L = [i for i in range(10)]
M = [i for i in range(10,0,-1)]
N = [a*b for a,b in zip(L,M)]
print(N)
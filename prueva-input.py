"""import functools


def f(j, i):
    s = (j) % i
    return s

lista_de_retorno = []

i = list(map(int,input().strip().split()))

i1 = i[0]
print(i1)
i2 = i[1]

for r in range (0, i1):
    r = list(map(int,input().strip().split()))
    rr = max(r)
    rr = rr**2
    lista_de_retorno.append(rr)
    
j = functools.reduce(lambda a, b: a + b, lista_de_retorno)

print(f(j,i2))
"""

from itertools import product
k, m = map(int, input().split())
array = []
for _ in range(k):
    array.append(list(map(int, input().split()))[1:])
result = 0
for combination in product(*array):
    result = max(sum([x * x for x in combination]) % m, result)
print(result)
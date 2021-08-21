def suma_iterativa(n=0):
 suma  =0
 for i in range (0,n+1):
     suma +=i
 return suma 

print(suma_iterativa(20))


def suma_rec(n=0):
 if n==0 :
     return 0
 else:
  return n + suma_rec(n-1)

print(suma_rec(-10))
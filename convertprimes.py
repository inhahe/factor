out = open('primes\\primes.txt','w')
for x in range(1,51):
  print ("...", end="")
  inf = open('primes\\primes'+str(x)+'.txt','r')
  inf.readline()
  out.write('\n'.join(inf.read().split())+'\n')
  print (x)


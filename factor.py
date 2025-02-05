##by Richard A. Nichols III, 2007
## 
##factor() returns the factorization of a given number.
## 
##primes.txt should be a newline-separated list of all prime numbers to
##an arbitrary limit.  i got my primes from
##http://primes.utm.edu/lists/small/millions/ and converted them to the above
##format.
## 
##it runs pretty fast up to a certain size input (10**19, for me) and then 
##it goes into diskswapping hell.
##edit: the above comment was made so long ago I had to convert this program from Python 2 to Python 3

# optimize reading from file

import sys
inf = open('primes.txt','r')
primes = [int(inf.readline())]
primesset = set(primes)

def factor(number, factors=[], lpi=0):
  global primes, primesset
  if number in primesset:
    return factors+[number] if factors else []
  sqrt = int(number ** .5)
  pi = lpi
  prime = primes[pi]
  while prime <= sqrt:
    if pi==len(primes):
      p = inf.readline()
      if p=='' or p=='\n': raise ValueError("--Cannot factor because the prime numbers list has been exhausted--")
      prime = int(p)
      primes += [prime]
      primesset.add(prime)
    else:
      prime = primes[pi]
    if number % prime == 0:
      return factor(number/prime, factors+[prime], pi)
    pi += 1
  return factors+[int(number)] if factors else [] 


if __name__ == "__main__":


  if len(sys.argv)==2:
    try: factors = factor(int(sys.argv[1]))
    except ValueError as e: print (e.args[0])
    else: print ('['+', '.join(str(f) for f in factors)+']'if factors else "prime")
  else:
    for x in range(18):
      number = int('1'*(x+1))
      print()
      print(number)
      try: factors = factor(number)
      except ValueError as e: print(e.args[0])
      else: print ('['+', '.join(str(f) for f in factors)+']' if factors else "prime")

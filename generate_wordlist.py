import itertools
import md5

tokens = [
  "abv", 
  "123", 
  "password", 
  "admin"
]

for i in range(1, len(tokens) + 1):
    for p in itertools.permutations(tokens, i):
        print "".join(p)

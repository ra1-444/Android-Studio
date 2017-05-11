import math
#!/usr/bin/python -u
import random,string
#BNZQ:8o149b15764q471k2533971t6w78liec
#flag = "FLAG:"+open("flag", "r").read()[:-1]
encflag ="" 
flag = "TUPQ:6o131y75525j229k8164784d1c12rsom"
random.seed("random")
for c in flag:
  if c.islower():
    #rotate number around alphabet a random amount
    encflag += chr((ord(c)-ord('a')+random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
    encflag += chr((ord(c)-ord('A')+random.randrange(0,26))%26 + ord('A'))
  elif c.isdigit():
    encflag += chr((ord(c)-ord('0')+random.randrange(0,10))%10 + ord('0'))
  else:
    encflag += c
    print "     a a                     BNZQ:8o149b15764q471k2533971t6w78liec "
print "Unguessably Randomized Flag: "+encflag
import sys
print(sys.version)
#import math
pie=math.pi
print pie

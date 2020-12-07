# Try try but don't cry
Basic crypto challenge. We get two files **chall.py** and **chall.txt**

### chall.py
```
import random
def xor(a,b):
  l=""
  for i in range(min(len(a), len(b))):
    l+=chr(ord(a[i]) ^ ord(b[i]))
  return l

def encrypt(flag):
  l=random.randrange(2)
  if(l==0):
    return flag.encode('base64')
  elif(l==1):
    return flag.encode('hex')
  

flag="################"
assert(len(flag)==22)
c=xor(flag[:11], flag[11:])
c=c.encode('hex')

n=random.randint(1,20)
#print(n)

for _ in range(n):
  c=encrypt(c)

f=open('chall.txt', 'w')
f.write(c)
f.close()

```

Lets go through the code and make points:
1. It asserts that the length of the flag to be 22.
2. Then it xors the first half of the flag with second half of the flag(losing bits here).
3. Then it generates a random number between 1 and 20, inclusive, and for that many times it calls the encrypt function, inside which it again generates a random number, which can be 1 or 2, and according to that random value either hex encode the flag or base64 encode the flag.
4. Finally it writes the encrypted flag into the [chall.txt](https://github.com/DaBaddest/CTF-Writeups/blob/master/boot2root%202020/Try%20try%20but%20don't%20cry/chall.txt) file.

So the solution is straight forward, we can just try to decrypt the encrypted flag with both the options and see which one makes more sense.

For this I am using **python2** because it uses regular strings and makes things a bit easy

Script to brute force
```
import base64
with open('chall.txt') as f:
  d = f.read()

for i in range(20):
  if len(d) == 11:
    break
  try:
    d = d.decode('hex')
  except:
    c = len(d) % 4
    for _ in range(c):
      d += b'='
    d = base64.b64decode(d)
print(d, len(d))
```

Which gives out the encrypted the flag as ```'\x03^D\x15A\x06\x06\x0c\x17\x18\x1b'```

As mentioned before, we are losing 11 bytes of the flag because of the xor operation, but xor is reversible. Bruteforcing is not a good method, but we know part of plaintext so we can do a known plaintext attack

```
Length of the flag is 22
We know the initial 10 bytes "b00t2root{" ,which is the flag format
b00t2root{xxxxxxxxxxxx
x is unknown
```

So we can just use the flag format to recover 10 more bytes.

The following script to brute force is using **python3**
```
plaintext = b'b00t2root{'
s = b'\x03^D\x15A\x06\x06\x0c\x17\x18\x1b'

o = ''
for idx in range(10):
  for i in range(32, 127):
    if i ^ plaintext[idx] == s[idx]:
      o += chr(i)
print(o)
```

We get 10 more bytes```antasticcc```


So in total we have 20 bytes, 2 bytes are missing. The last one is '}' beacuse of the flag format

```
b00t2root{Xantasticcc}
X is unknown
```

We can use the last char to decrypt the only missing byte, but we can just take a guess the it can be **f** or **F** because it makes sense and indeed it is the flag
```
b00t2root{fantasticcc}
```

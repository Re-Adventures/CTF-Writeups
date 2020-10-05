# Totem

Totem was in the crypto category.

Well it didnt actually use any serious crypto stuff but just simple cipher techniques.

In this challenge we got **totem-template-64570ca140218e167da3995184bc89a4.py** having the contents

```
# You can install these packages to help w/ solving unless you have others in mind
# i.e. python3 -m pip install {name of package}
from pwn import *
import codecs
from base64 import b64decode
from string import ascii_lowercase

HOST = ''
PORT = 0

r = remote(HOST,PORT)

def bacon(s):
    # Do this

def rot13(s):
    # And this

def atbash(s):
    # And this one

def Base64(s):
    # Lastly this one

if __name__ == '__main__':
    count = 0
    while True:     
        r.recvuntil('Method: ')
        method = r.recvuntil('\n').strip()
        r.recvuntil('Ciphertext: ')
        argument = r.recvuntil('\n').strip()

        result = globals()[method.decode()](argument.decode())  # :)

        r.recv()
        r.sendline(result.encode())
        count += 1
        if count == 1000:
            print(r.recv())
            exit(0)
```
This code has everything, all the networking stuff is also already implemented, we just need to implement the cipher methods.

The problem I got here is that it is using pwntools for networking purposes, but I am using **Windows** and pwntools is not available for Windows, so I had to implement all the networking stuff by myself.

First I will implement the networking stuff using the telnetlib library in python.

```
import telnetlib
import base64
import sys

Host, Port = 'chal.ctf.b01lers.com', 2008
T = telnetlib.Telnet(Host,Port)

def recv(s):
  return T.read_until(s.encode('charmap'), timeout=5)

def send(s):
  T.write(s.encode('charmap') + b"\n")
```

It is simple network programming, first I initiate the connection using ```telnetlib.Telnet``` function, passing the Host and the Port

I have defined the two functions **recv** and **send** as a favour to myself because now I can just pass the string and it will do all the encoding-decoding stuff.

After this we just need to define the cipher functions.

1. [Baconian cipher](https://en.wikipedia.org/wiki/Bacon%27s_cipher)
```
def bacon(s):
  d1 = {'AAAAA' : 'A','AAAAB' : 'B',  'AAABA' : 'C',  'AAABB' : 'D',  'AABAA' : 'E',  'AABAB' : 'F',  'AABBA' : 'G',  'AABBB' : 'H',  'ABAAA' : 'I',  'ABAAB' : 'J',  'ABABA' : 'K',  'ABABB' : 'L',  'ABBAA' : 'M',  'ABBAB' : 'N',  'ABBBA' : 'O',  'ABBBB' : 'P',  'BAAAA' : 'Q',  'BAAAB' : 'R',  'BAABA' : 'S',  'BAABB' : 'T',  'BABAA' : 'U',  'BABAB' : 'V',  'BABBA' : 'W',  'BABBB' : 'X',  'BBAAA' : 'Y',  'BBAAB' : 'Z'}

  if 0 != len(s) % 5:
    exit("Odd length string, it should be a multiple of 5")

  st = ''
  for i in range(0, len(s), 5):
    temp = s[i:i+5]
    st += d1[temp].lower()
  return st
```

2. [ROT13](https://en.wikipedia.org/wiki/Caesar_cipher)
```
def rot13(s):
  key = 13
  temp = ''
  for i in s:
    if 0x40 < ord(i) < 0x41 + 26:
      temp += chr(((ord(i) + key - 0x41) % 26) + 0x41)
    elif 0x60 < ord(i) < 0x61 + 26:
      temp += chr(((ord(i) + key - 0x61) % 26) + 0x61)
    else:
      temp += i
  return temp
```

3. [Atbash cipher](https://en.wikipedia.org/wiki/Atbash)
```
def atbash(s):
  _upper = ''.join([chr(x) for x in range(0x41, 0x41+26)])[::-1]
  _lower = ''.join([chr(x) for x in range(0x61, 0x61+26)])[::-1]
  res = ''
  for i in s:
    if 0x41 <= ord(i) <= 0x5b:
      res += _upper[ord(i) - 0x41]
    elif 0x61 <= ord(i) <= 0x7b:
      res += _lower[ord(i) - 0x61]
  return res
```

4. [Base64](https://en.wikipedia.org/wiki/Base64)*Encoding*
```
def Base64(s):
  return base64.b64decode(s).decode()
```

The whole solution script is as follows
```
# ncat -v chal.ctf.b01lers.com 2008

import telnetlib
import base64
import sys

Host, Port = 'chal.ctf.b01lers.com', 2008
T = telnetlib.Telnet(Host,Port)


def recv(s):
  return T.read_until(s.encode('charmap'), timeout=5)

def send(s):
  T.write(s.encode('charmap') + b"\n")


def bacon(s):
  d1 = {'AAAAA' : 'A','AAAAB' : 'B',  'AAABA' : 'C',  'AAABB' : 'D',  'AABAA' : 'E',  'AABAB' : 'F',  'AABBA' : 'G',  'AABBB' : 'H',  'ABAAA' : 'I',  'ABAAB' : 'J',  'ABABA' : 'K',  'ABABB' : 'L',  'ABBAA' : 'M',  'ABBAB' : 'N',  'ABBBA' : 'O',  'ABBBB' : 'P',  'BAAAA' : 'Q',  'BAAAB' : 'R',  'BAABA' : 'S',  'BAABB' : 'T',  'BABAA' : 'U',  'BABAB' : 'V',  'BABBA' : 'W',  'BABBB' : 'X',  'BBAAA' : 'Y',  'BBAAB' : 'Z'}

  if 0 != len(s) % 5:
    exit("Odd length string, it should be a multiple of 5")

  st = ''
  for i in range(0, len(s), 5):
    temp = s[i:i+5]
    st += d1[temp].lower()
  return st

def rot13(s):
  key = 13
  temp = ''
  for i in s:
    if 0x40 < ord(i) < 0x41 + 26:
      temp += chr(((ord(i) + key - 0x41) % 26) + 0x41)
    elif 0x60 < ord(i) < 0x61 + 26:
      temp += chr(((ord(i) + key - 0x61) % 26) + 0x61)
    else:
      temp += i
  return temp

def atbash(s):
  _upper = ''.join([chr(x) for x in range(0x41, 0x41+26)])[::-1]
  _lower = ''.join([chr(x) for x in range(0x61, 0x61+26)])[::-1]
  res = ''
  for i in s:
    if 0x41 <= ord(i) <= 0x5b:
      res += _upper[ord(i) - 0x41]
    elif 0x61 <= ord(i) <= 0x7b:
      res += _lower[ord(i) - 0x61]
  return res

def Base64(s):
  return base64.b64decode(s).decode()



l = ["bacon","rot13","atbash","Base64"]
funcs = [bacon,rot13,atbash,Base64]


for j in range(1000):
  data = recv('Input: ')

  data = data.split(b"\n")
  #print(data)

  method = data[0].split(b': ')[1].decode()
  cipher = data[1].split(b': ')[1].decode()

  #print(method, cipher)
  for i in range(len(l)):
    if method == l[i]:
      data = funcs[i](cipher)
      break
  print(f'{j} : {data}')
  send(data)

data = recv("\n")
sys.stdout.write(data.decode())
sys.stdout.flush()

data = recv("\n")
sys.stdout.write(data.decode())
sys.stdout.flush()

data = recv("\n")
sys.stdout.write(data.decode())
sys.stdout.flush()

```

This script takes around 10 min to complete even when using pypy and gives out the flag
```
ctf{4n_313g4nt_s01ut10n_f0r_tr4cking_r341ity}
```

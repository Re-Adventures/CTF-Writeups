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

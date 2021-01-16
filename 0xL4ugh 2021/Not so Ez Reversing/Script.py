import subprocess, os

rand_vals = [int(i) for i in open("values_linux").read().split(',')]
fname = "Photo.jpg"

with open("data.dat", "rb") as f:
  fp = f.read()
os.system(f'del {fname}')

o = ''
for i in range(len(fp)):
  tmp = rand_vals[i]
  if tmp == 0 or tmp == 2:
    o += chr(fp[i] ^ 1)
  else:
    o += chr(fp[i])

with open(f"{fname}", 'wb') as f:
  f.write(o.encode('charmap'))

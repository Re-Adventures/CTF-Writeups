import zipfile, os
c=32949
n=64741
e=42667
for m in range(n):
  temp = pow(m, e, n)
  if temp == c:
    key = m

print(key)
p = str(key).encode()
with zipfile.ZipFile('flag.zip') as zf:
  try:
    zf.extractall(pwd=p)
    print("found ", p)
  except:
    print('Tried', p)
os.system("type flag.txt")

# Little RSA

As the name suggests it's a [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) problem.

We get two files, a text file **a.txt** and a **flag.zip** which is password protected.

The goal is to find password of the zip file.

The file provided **a.txt** has the following contents:
```
c=32949
n=64741
e=42667
```
CHANGE
CHANGE
We can do it using the formal way for which you can look at this [Writeup](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

In this approach I didn't do it in the formal way because n is too small

We can just find the Key (M) by bruteforcing, for which I used the following script:
```
for m in range(n):
  temp = pow(m, e, n)
  if temp == c:
    key = m

print(f'key = {key}')
```
Which prints out
```
key = 18429
```

Now we have the key we can simply unzip the file manually but I wrote a script for it
```
with zipfile.ZipFile('flag.zip') as zf:
  try:
    zf.extractall(pwd=p)
    print("found ", p)
  except:
    print('Tried', p)
```

The whole script:
```
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
```

```
csictf{gr34t_m1nds_th1nk_4l1ke}
```

# Fibonacci

In this challenge we got a **7z** file, but it is broken.

When we run file command on it, it doesnt recognize any file format and just says it is data 

```
D:\CTF\Affinity\Fibonacci>file Fibonacci.7z
Fibonacci.7z; data
```

Next step would be to take a look at the file using hexdump
```
D:\CTF\Affinity\Fibonacci>hexdump -C Fibonacci.7z | head
00000000  42 42 42 42 37 42 7a bc  42 af 27 1c 00 42 04 c9  |BBBB7Bz¼B_'..B.É|
00000010  33 6d e5 69 05 42 00 00  00 00 00 00 5a 00 00 00  |3måi.B......Z...|
00000020  00 00 42 00 00 77 9e d7  14 e0 0b e2 05 61 5d 00  |..B..wzx.à.â.a].|
00000030  21 68 b4 90 09 c2 64 42  c0 64 04 61 73 78 6c 59  |!h'.       AdBAd.asxlY|
00000040  04 1b 7e c3 e0 75 08 cf  3b 81 a1 86 1f 0c 25 57  |..~Aàu.I;.¡+..%W|
00000050  fd ed 72 e7 04 b6 20 eb  a2 42 dc c7 e2 f1 ee 76  |yírç.¶ ë¢BÜÇâñîv|
00000060  40 7f 6f a8 09 dc e8 db  19 d4 ea 35 07 43 14 a5  |@.o"       ÜèU.Oê5.C.¥|
00000070  e9 62 5c 96 b4 85 32 9f  e0 ea 4c 10 fc 8f 44 93  |éb\-'.2YàêL.ü.D"|
00000080  54 07 06 31 06 6e 79 38  eb c2 7e 52 a1 7f a5 47  |T..1.ny8ëA~R¡.¥G|
00000090  42 46 65 02 18 9a ce 8c  6a e2 46 9c 8f 93 0f 57  |BFe..sIOjâFo.".W|
```

The header is clearly broken, because the header of 7zip file is  ```37 7A BC AF 27 1C```. But fixing the header doesnt work.

Again by looking closely at the hexdump of file, we see character **B** multiple times and that too at specific indices ```0 1 2 3 5 ...``` which is Fibonacci series, which is the title of the challenge, so we knew we are heading towards the right direction.

So we just need to remove the bytes at that specific index from the file Fibonacci.7z to fix the file.

We can do it by hand, but a simple python script would be helpful

```
# Generating Fibonacci sequence
fib = [0, 1]
for i in range(2, 30):
  fib.append(fib[i-2] + fib[i-1])
fib.pop(1)  # because 1 in repeated twice in the Fibonacci

dat = bytearray(open('Fibonacci.7z', 'rb').read())

buf = b''
i = 0
for j in range(len(dat)):
  if j == fib[i]:
    i += 1
    continue
  else:
    buf += chr(dat[j]).encode('charmap')

open('Output.7z', 'wb').write(buf)
```

Now if we run file command on the **Output.7z** file, it correctly identifies it as a 7zip archieve.

Extracting the Output.7z file gives a file named **Fibonacci** which is a text file, and on the last line of it is the flag.

```"AFFCTF{Hitchhiker}," said Deep Thought, with infinite majesty and calm.ΓÇ¥```

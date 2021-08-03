# Signals

Caterogy: Reverse engineering
Description: *This program is sending me mixed signals...*

# Basic Analysis

In this challenge we get a 64-bit Linux executable

```cmd
D:\CTF\UIUCTF\signals>file signals
signals; ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 3.2.0, not stripped
```


# Analyzing the binary

Opening the file in binary ninja

We see something interesting
```asm
000012a0  lea     rdi, [rel code]
000012a7  call    make_executable
```
We see a call to `make_executable` with `code` as the parameter

Disassembling the make_executable function, one instruction caught my attention
```asm
00001248  call    mprotect
```

So make_executable is calling `mprotect` with `code`. mprotect is used to change the permissions of some area of the memory, i.e. we can make some read-only data to executable too.

My guess was that it is making the segment executable where `code` variable is stored.


Analyzing the main function more
```asm
000012f5  mov     rax, qword [rbp-0x20 {argv}]
000012f9  mov     rax, qword [rax+0x8]
000012fd  mov     rcx, rax
00001300  lea     rdx, [rel code]
00001307  mov     eax, 0x0
0000130c  call    rdx  {code}
```

We see that it loads argv[1] (our input) into rcx.

And then it loads the address of code variable into rdx, and then jumps there.

Jumping to `code` variable, binary ninja doesn't show it as a function, we have to press `P` to make function at that address.

And indeed it is some valid code

```asm
code:
00004020  lea     rax, [rel data_4435]
00004027  mov     dl, byte [rcx]
00004029  xor     rbx, rbx  {0x0}

0000402c  xor     byte [rax+rbx], dl
0000402f  inc     rbx
00004032  cmp     rbx, 0x1d
00004036  jne     0x402c

00004038  inc     rcx
0000403b  jmp     rax  {data_4435}
```

In this code, it first loads some data `data_4435` into rax. That rel means that it is relative to RIP. Binary ninja shows it like that, the actual instruction looks like `LEA RAX, [RIP+0x15d5]`.

Then it loads a byte from rcx into dl, remember that the input that we pass (argv[1]) was stored in the rcx register.

Then it clears out rbx register and use that register as a counter for the loop. In this loop, it loads a byte from the `data_4435` and xors it with our input, i.e. it is decrypting it and it jumps to that decrypted code.

The high level representation of that code would look like
```C
rcx = &argv[1];   //our input
rax = &data_4435;
for(rbx=0; rbx<0x1d; ++rbx){
  rax = *rax ^ *rcx;
  rax++;
}
rcx++;
rax();
```

Also notice that it increments rcx at the end. Which means that now rcx is pointing to second character of our input.

As we know that the flag format is `uiuctf{...}`, so the first character has to be `u` or maybe `U`.

So we can write a simple python code to decrypt this

```py
def decrypt(data, val):
  return b''.join([chr(i ^ val).encode('charmap') for i in data])

with open('signals', 'rb') as fp:
  dat = fp.read()

base = 0x1000
start = 0x0004435
end = start + 0x1d

key = ord`('u')

code = decrypt(dat[start:end+1], key)

open('layer1', 'wb').write(
    dat[:start] +
    code + 
    dat[end:]
  )

```

Opening the `layer1` file in binary ninja and jumping to code

```asm
00004435  lea     rax, [rel data_5a11]
0000443c  mov     dl, byte [rcx]
0000443e  xor     rbx, rbx  {0x0}

00004441  xor     byte [rax+rbx], dl
00004444  inc     rbx
00004447  cmp     rbx, 0x1d
0000444b  jne     0x4441

0000444d  inc     rcx
00004450  jmp     rax  {data_5a11}
```


Indeed, it decrypted some more meaningful code. One thing to note here is that the decrypted code looks similar to the code that we saw earlier, only the data that is to be decrypted is different `data_5a11`.

So now it will decrypt the code with second letter of our input, i.e. `i`.

We can just run our [layer1 code]() with some changes into the offset and key, it will decrypt the second layer.

```asm
LEA RAX, [RIP-0x9f9]
MOV DL, [RCX]
XOR RBX, RBX
XOR [CR4:RAX+RBX], DL
INC RBX
CMP RBX, 0x1d
JNZ 0x100c
INC RCX
JMP RAX
```

And again the similar code is decrypted.

**Lets assume that it will be decrypting the same code over and over again for the input characters.**

So we just need to find the characters that will decrypt the code which looks similar to our previous code.

But doing this character by character and then opening it in a disassembler takes too much time, we need to somehow automate this.

## Possible Approaches

1. Symbolic execution: tools like `angr` or `manticore`can be used for this approach but these are automatic solvers, and it sounds boring to just run a simple script to solve a crackme.

2. Dynamic analysis: this would require us to run the program and count the number of instructions executed. For the correct input, it should execute the highest number of instructions.

3. Static analysis: using a python code to decrypt layer by layer based on the correct input.


## Dynamic Analysis

As the program is decrypting itself and if the characters are correct, it executes more instructions, so for every character we execute more instructions than before.

So we can just use the `perf` tool which is capable of counting the number of instructions executed.

I got this idea from [this](https://dustri.org/b/defeating-the-recons-movfuscator-crackme.html) write-up. According to the write-up, if we the following command, it will give us the count of the instructions.

```bash
perf stat -x, -e instructions:u ./signals
```

But for some reason, it was giving me the error
`The instructions event is not supported.`

If this would have worked, we could just change the program name in the code that was in that write-up, and it would have given us the flag.

## Static Analysis

**Lets assume that it will be decrypting the same code over and over again for the input characters.**

Then we just need the offsets of the data to be decrypted and we can just compare the parts of the code to the previous one.

Lets start writing the code.

1. Lets just define our decrypt function and read the binary

```py
def decrypt(d, val):
  return b''.join([chr(i ^ val).encode('charmap') for i in d])

with open('signals', 'rb') as fp:
  dat = fp.read()

```

2. Getting some offsets from the file

```py
code_addr = 0x4435
base = 0x1000
```

The `code_addr` is the address of the data which is to be decrypted.
The address at which the binary is loaded is stored at `base` variable. To get the base address, just run the following command

```cmd
D:\CTF\UIUCTF 2021\signals>objdump -d signals

signals:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <_init>:
```

The first address (0x1000) is the base address.


3. Then we can just bruteforce it char by char. But how will we get the disassembly. There are three methods I can think of:

a) **objdump**: to get the disassembly, but objdump just decodes the text section, and our code is not in the text section of the binary


b) **ndisasm**: we can get the disassembly using the following command
```bash
ndisasm -b64 file
```

It requires us to save the code in a file, and then pass it.


c) **distorm3**: [distorm3](https://github.com/gdabah/distorm/) is a python libraby which is capable of disassembling code. I used this approach


Now continuing writing the script

```py
import distorm3
def decrypt_inst(data):
  return [i[2] for i in distorm3.Decode(0x1000, data, distorm3.Decode64Bits)]

flag = ''  # Will store the flag
while 1:
  for ch in range(32, 127):  # Printable range
    address = code_addr - base
    code = decrypt(dat[address:address+0x1d], ch)
    inst = decrypt_inst(code)
    if 'JMP RAX' in inst and 'LEA' in inst[0]: # if character found
      flag += chr(ch)
      print(flag)
      off = inst[0].split('LEA RAX, [RIP')[1].replace('0x','').replace(']', '') # getting address of next data
      code_addr = code_addr + int(off, 16)
      break
  if 126 == ch: # If character not found
    exit("ERROR")
```

Code looks fine lets run it

```cmd
D:\CTF\UIUCTF 2021\signals>python script.py
u
ERROR
```

It prints the first character correctly, but then it errors out

So the problem was that, it was getting the code_addr wrong, it was getting the address 0x5a0a instead of 0x5a11.

It is beacuse the first instruction `00004435  lea     rax, [rel data_5a11]` is 7 bytes long, so we have to add 7 to the code_addr

The [final script](https://github.com/DaBaddest/CTF-Writeups/blob/master/UIUCTF%202021/signals/script.py) should be

```py
import distorm3
def decrypt_inst(data):
  return [i[2] for i in distorm3.Decode(0x1000, data, distorm3.Decode64Bits)]

def decrypt(d, val):
  return b''.join([chr(i ^ val).encode('charmap') for i in d])

with open('signals', 'rb') as fp:
  dat = fp.read()

base = 0x1000
code_addr = 0x4435
flag = ''
while 1:
  for ch in range(32, 127):
    address = code_addr - base
    code = decrypt(dat[address:address+0x1d], ch)
    inst = decrypt_inst(code)
    if 'JMP RAX' in inst and 'LEA' in inst[0]:
      flag += chr(ch)
      print(flag)
      off = inst[0].split('LEA RAX, [RIP')[1].replace('0x','').replace(']', '')
      code_addr = code_addr + int(off, 16) + 7
      break
  if 126 == ch:
    exit("ERROR")

```

Running the script

```cmd
D:\CTF\UIUCTF 2021\signals>python script.py
u
ui
uiu
uiuc
uiuct
uiuctf
uiuctf{
uiuctf{a
uiuctf{an
uiuctf{ano
uiuctf{anot
uiuctf{anoth
uiuctf{anothe
uiuctf{another
uiuctf{another_
uiuctf{another_c
uiuctf{another_ct
uiuctf{another_ctf
uiuctf{another_ctf_
uiuctf{another_ctf_a
uiuctf{another_ctf_an
uiuctf{another_ctf_ano
uiuctf{another_ctf_anot
uiuctf{another_ctf_anoth
uiuctf{another_ctf_anothe
uiuctf{another_ctf_another
uiuctf{another_ctf_another_
uiuctf{another_ctf_another_f
uiuctf{another_ctf_another_fl
uiuctf{another_ctf_another_fla
uiuctf{another_ctf_another_flag
uiuctf{another_ctf_another_flag_
uiuctf{another_ctf_another_flag_c
uiuctf{another_ctf_another_flag_ch
uiuctf{another_ctf_another_flag_che
uiuctf{another_ctf_another_flag_chec
uiuctf{another_ctf_another_flag_check
uiuctf{another_ctf_another_flag_checke
uiuctf{another_ctf_another_flag_checker
ERROR
```

It errors out but almost prints the flag.

As we know that the flag format is `uiuctf{...}`, so we can just add the `}` and try the flag

And indeed it is the correct flag

```
uiuctf{another_ctf_another_flag_checker}
```

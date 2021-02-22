# Too Much

Desc: *How about reversing 200 functions at once?? Try yourself!!!*

Reversing challenge from darkCON CTF 2021

The file we get in this challenge binary [file](https://github.com/DaBaddest/CTF-Writeups/blob/master/darkCON%20CTF%202021/Too%20Much/rev)

## Recon

On running file on it, it reveals its a 64-bit ELF
```bash
D:\CTF\DarkConCTF\Too Much>file rev
rev; ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 3.2.0, not stripped
```

On running strings on it, we see some intresting strings
```bash
Congrats!!! You have cracked my code.
Please try harder!!!!
:*3$"
GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8060
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
rev.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
f6037610
f3890123
f554708
f306999
f3371760
f3189640
f1853358
f4356041
f1103067
f5663288
f846013
f8974270
_ITM_deregisterTMCloneTable
f3873488
f6594036
f3574708
f4692198
f2161814
f3404320
puts@@GLIBC_2.2.5
f3273483
f2033367
f9565003
f8976878
f9397951
f7138486
f7656586
f8346581
f8769072
f5150019
f7824321
f7994952
...
```

Opening the file in binaryninja, we see a long list of function and the weird strings are actually functions, we can see in the description of the challenge that there are 200 functions.

So 200 functions which check the flag character by character, so the flag has to be 200 characters long.


We have to start somewhere so Lets start by analyzing any random function from the 200 intresting functions.


After looking after 3-4 functions, the code of each of them is similar only just a slight difference on the checked value.

```c
bool function(){
  (16 * a1) + (a1 >> 4) == (int)some_const_value;
}
```

So the code is same for all 200 values just the const value is changing.

So from here the challenge is trivial, because it checks the flag character by character so we can easily bruteforce it and code is the same, but the only challenge is to extract all the const values from the 200 functions.

One solution could be just to use some tools like **angr** or **manticore** but I dont know how to use them so thats off the list.

## Solution

Again on opening taking a look at the diasassembly, we can clearly see a recurring pattern in the functions

```asm
0000000000001189 <f122323>:
...
    11ac: 83 f8 46              cmp    eax,0x46
    11af: 0f 94 c0              sete   al
...
000000000000120a <f3113161>:
...
    122d: 3d b6 00 00 00        cmp    eax,0xb6
    1232: 0f 94 c0              sete   al
...
```

There is a cmp for one character and then a sete instruction, so we can just use objdump to dump the disassembly of binary and then write a python script to get all the values

```bash
objdump -M intel -a rev > dump.asm
```

Now we can easily operate on the [dump.asm](https://github.com/DaBaddest/CTF-Writeups/blob/master/darkCON%20CTF%202021/Too%20Much/dump.asm) file

I wrote a short python [script](https://github.com/DaBaddest/CTF-Writeups/blob/master/darkCON%20CTF%202021/Too%20Much/Solution.py) to do so
The following script only works assuming that the functions are in order, if they were out of order then we'll have to take a different approach

```py
with open("dump2.asm") as fp:
  dat = fp.readlines()


# Getting the values
inst = []
for i in range(len(dat)):
  if ("sete   al" in dat[i]) and ("cmp    eax," in dat[i-1]):
    inst.append(dat[i-1])

vals = []
for i in inst:
  vals.append(int(i.split("eax,0x")[1], 16))


# Bruteforcing char-by-char
flag = ''
for v in vals:
  for i in range(32, 127):
    if ((16 * i) + (i >> 4)) & 0xff == v:
      flag += chr(i)
      break

assert 200 == len(flag) # Since there are 200 functions

print(flag)
```

```
darkCON{4r3_y0u_r34lly_th1nk1n9_th4t_y0u_c4n_try_th15_m4nu4lly???_Ok_I_th1nk_y0u_b3tt3r_us3_s0m3_aut0m4t3d_t00ls_l1k3_4n9r_0r_Z3_t0_m4k3_y0ur_l1f3_much_e4s13r.C0ngr4ts_f0r_s0lv1in9_th3_e4sy_ch4ll3ng3}
```
